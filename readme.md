# growatt API
Basic docker file for running an API to allow openhab to log powerusage gtom the growatt server.

Rename the envfile.sample to envfile and add your credentials for the growatt server.

Needs docker installed on the host and the JSONPath Transformation addon installed in openhab

Example docker launch following the build:
`docker run --env-file ./envfile -p 5000:5000 -it gwdocker`

Thanks to indykoning for the python code to connect to growatt servers https://github.com/indykoning/PyPi_GrowattServer

Code to config the HTTP URL Thing in openhab:

```
UID: http:url:0b7207acc3
label: HTTP URL Thing
thingTypeUID: http:url
configuration:
  authMode: BASIC
  ignoreSSLErrors: false
  baseURL: http://locahost:5000/reading
  delay: 0
  stateMethod: GET
  refresh: 60
  commandMethod: GET
  contentType: application/json
  timeout: 5000
  bufferSize: 2048
channels:
  - id: power
    channelTypeUID: http:number
    label: Power
    description: Power in Watts
    configuration:
      mode: READONLY
      stateTransformation: JSONPATH:$.plant_info.deviceList[0].power
```
