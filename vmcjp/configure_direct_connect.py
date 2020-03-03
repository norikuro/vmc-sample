#!/usr/bin/env python

import requests
import atexit

from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

def get_nsx_app_client(token, org_id, sddc_id):
  session = requests.Session()
  nsx_app_client = create_nsx_vmc_app_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id,
      session=session
  )
  atexit.register(session.close)
  return nsx_app_client

def main():
  token = "VMC_Refresh_Token_xxxxxxx"
  org_id = "VMC Org ID"
  sddc_id = "VMC SDDC ID"

  nsx_app_client = get_nsx_app_client(
      token, 
      org_id, 
      sddc_id
  )

  vifs = nsx_app_client.infra.direct_connect.Vifs.list().results
  
  #we will attach all available VIFs to SDDC.
  for vif in vifs:
    try:
      vifs.create(vif.id, "ATTACH")
      print("VIF id:{} is attached to this SDDC".format(vif.id))
    except Exception as e:
      print("Failed to attach VIF, {}".format(e.message))

if __name__ == '__main__':
  main()
