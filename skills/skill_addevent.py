import requests
from datetime import datetime, timedelta
from flask import Flask, Response, request, json, render_template, Blueprint
import uuid
import json

skill_addevent = Blueprint('skill_addevent',__name__)


token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFEWHpaM2lmci1HUmJEVDQ1ek5TRUZFY1dIcHY3ZlpPSTB4NWp0S18xbERNd0pVZ1N5Nml2SlRHV2prY3l3U0tMOFBwc1BCRVRhQkk3ck9vMUNzR2dBSHdJQ0ZEVm5jSFlSckRYd05ieWx2VUNBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3Iiwia2lkIjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3In0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNTMyNDg5MjQ1LCJuYmYiOjE1MzI0ODkyNDUsImV4cCI6MTUzMjQ5MzE0NSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhJQUFBQUpuaFBPVUVLMzB0emRqaUZ5RXZBTElHM25CanNNU2Z4cEllRXU1dzJSczlzQ0p1R05LVDJyakIwcmw1T3BkRWlQODZxZkIwMXJYUkphYUlFOUlldWNnPT0iLCJhbXIiOlsicnNhIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIGV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJkZXZpY2VpZCI6IjkyZmIyODQzLWIwMzYtNDRkNC1hMWU2LWViMDZiNzdkZmIyNCIsImZhbWlseV9uYW1lIjoiWmlsYmVyc3RlaW5lIiwiZ2l2ZW5fbmFtZSI6IklseWEiLCJpcGFkZHIiOiIxMzEuMTA3LjE2MC4xNTAiLCJuYW1lIjoiSWx5YSBaaWxiZXJzdGVpbmUiLCJvaWQiOiJhMmE4OTkyYi01NzRlLTQxOTItYTIwOS1kMmM1YzQ0ZDA5NWEiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjEyNzUyMTE4NC0xNjA0MDEyOTIwLTE4ODc5Mjc1MjctMzA2NzMyNTUiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzdGRkVBODc2OUUyQiIsInNjcCI6IkNhbGVuZGFycy5SZWFkV3JpdGUgQ29udGFjdHMuUmVhZFdyaXRlIERldmljZU1hbmFnZW1lbnRBcHBzLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRBcHBzLlJlYWRXcml0ZS5BbGwgRGV2aWNlTWFuYWdlbWVudENvbmZpZ3VyYXRpb24uUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudENvbmZpZ3VyYXRpb24uUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50TWFuYWdlZERldmljZXMuUHJpdmlsZWdlZE9wZXJhdGlvbnMuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50TWFuYWdlZERldmljZXMuUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50UkJBQy5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50UkJBQy5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRTZXJ2aWNlQ29uZmlnLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRTZXJ2aWNlQ29uZmlnLlJlYWRXcml0ZS5BbGwgRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRmlsZXMuUmVhZFdyaXRlLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIElkZW50aXR5Umlza0V2ZW50LlJlYWQuQWxsIE1haWwuUmVhZFdyaXRlIE1haWxib3hTZXR0aW5ncy5SZWFkV3JpdGUgTm90ZXMuUmVhZFdyaXRlLkFsbCBvcGVuaWQgUGVvcGxlLlJlYWQgcHJvZmlsZSBSZXBvcnRzLlJlYWQuQWxsIFNpdGVzLlJlYWRXcml0ZS5BbGwgVGFza3MuUmVhZFdyaXRlIFVzZXIuUmVhZEJhc2ljLkFsbCBVc2VyLlJlYWRXcml0ZSBVc2VyLlJlYWRXcml0ZS5BbGwgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsiZHZjX21uZ2QiLCJkdmNfY21wIiwiZHZjX2RtamQiLCJrbXNpIl0sInN1YiI6IktjMjUwZ01OS3RyLVo4RFBzMTZvNTROb2UzckRFMC1SQWt5QURlTGNxWHciLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1bmlxdWVfbmFtZSI6ImlsemlsYmVyQG1pY3Jvc29mdC5jb20iLCJ1cG4iOiJpbHppbGJlckBtaWNyb3NvZnQuY29tIiwidXRpIjoiS1FJSHFMN3N0MFNKSGN2YUFLRURBQSIsInZlciI6IjEuMCIsInhtc19zdCI6eyJzdWIiOiJnRlNRNzVuaTdIdkZDbWZIb3JEWnZVdXVZd0k2d1Vyb3VzR3c5OUFmNDEwIn19.t82DxEAGz_ca2_wGHC12TLq4O0y3cpT_wqDzB_UrRcnkiP8KKNrySr-4SXTvT8EjZjh1tevbaAuDZCEvPbBtT0BuN2SHZg4WefnI9FnuVRk0OZ79tMgK1EJTjxOa0DCM2gBEcNypMgTJNt7NW4eeWA6zcyxeFNWlmrUidtvnHYeNaxAS-9L-m7rkXtffcAbs-LhhCck4CKZtc2qeUqU9z4VC0sYm8snHiLiZ85q1imHN_5J4keuWSOnEqwKJ-4REPGx7uHjpnaiTEvPsDr68E_QG6-nHZRbWklUyMc3peGBdGLQG1pRdekQpduhMrhlosD0IMMvJaGszqQyha5NXlg'

# token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFEWHpaM2lmci1HUmJEVDQ1ek5TRUZFZ0duTHNUQVRxM0VYVW9IZkVpU0E0THp4TnE5dW9DaHgyZnlWTjhHNmFDOTVaSUZuWDV2dFpKRG5UNWlHVVFoYlNnYnltWkJfb3R3R0M4UlB6c2FLb0NBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3Iiwia2lkIjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3In0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNTMyMzkwNjE2LCJuYmYiOjE1MzIzOTA2MTYsImV4cCI6MTUzMjM5NDUxNiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhJQUFBQTlQUW9yTlBJdkVTbi9wUktWRFhlYlFPbzd4MjhOWXlIaWtiT2tGTEJtL21teHllRTVkL1lhem1LZTlIUTlvRW9sVCt5WHAwenEyS09DblN5U1RnTUxRPT0iLCJhbXIiOlsid2lhIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIGV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkphaW4iLCJnaXZlbl9uYW1lIjoiU2hsb2FrIiwiaW5fY29ycCI6InRydWUiLCJpcGFkZHIiOiIxMzEuMTA3LjE2MC41MiIsIm5hbWUiOiJTaGxvYWsgSmFpbiIsIm9pZCI6IjVlYTIwYzJhLTNhODctNDE5ZC1hOWRjLWY3MzlmMjZiMGRmNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0yMTI3NTIxMTg0LTE2MDQwMTI5MjAtMTg4NzkyNzUyNy0zMTY4MjEwOSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMDAwMEFBQkZGRTE5Iiwic2NwIjoiQ2FsZW5kYXJzLlJlYWRXcml0ZSBDb250YWN0cy5SZWFkV3JpdGUgRGV2aWNlTWFuYWdlbWVudEFwcHMuUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudEFwcHMuUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50Q29uZmlndXJhdGlvbi5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50Q29uZmlndXJhdGlvbi5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5Qcml2aWxlZ2VkT3BlcmF0aW9ucy5BbGwgRGV2aWNlTWFuYWdlbWVudE1hbmFnZWREZXZpY2VzLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRSQkFDLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRSQkFDLlJlYWRXcml0ZS5BbGwgRGV2aWNlTWFuYWdlbWVudFNlcnZpY2VDb25maWcuUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudFNlcnZpY2VDb25maWcuUmVhZFdyaXRlLkFsbCBEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZFdyaXRlLkFsbCBGaWxlcy5SZWFkV3JpdGUuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgSWRlbnRpdHlSaXNrRXZlbnQuUmVhZC5BbGwgTWFpbC5SZWFkV3JpdGUgTWFpbGJveFNldHRpbmdzLlJlYWRXcml0ZSBOb3Rlcy5SZWFkV3JpdGUuQWxsIG9wZW5pZCBQZW9wbGUuUmVhZCBwcm9maWxlIFJlcG9ydHMuUmVhZC5BbGwgU2l0ZXMuUmVhZFdyaXRlLkFsbCBUYXNrcy5SZWFkV3JpdGUgVXNlci5SZWFkQmFzaWMuQWxsIFVzZXIuUmVhZFdyaXRlIFVzZXIuUmVhZFdyaXRlLkFsbCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IlNyNm51V0N1T2NiQ3U3MnhYY2xfM051RlB4WFNhc05KZVFUd2hiNjZJdnMiLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1bmlxdWVfbmFtZSI6InQtc2hqYUBtaWNyb3NvZnQuY29tIiwidXBuIjoidC1zaGphQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJEbHYyUmNQS3gwYWljUi1CeG9BQ0FBIiwidmVyIjoiMS4wIiwieG1zX3N0Ijp7InN1YiI6ImhTUk1Dd3NneGdJMVV4M0NNMC1HVnRIODlDX0FublhYdmcxUHExOGo3cjAifX0.UQLkiqlYybEqQ0RDcCH_-6GH1BwycFeBnonFgS2zngP42ykt5zDgv2qwUwvPjYK78Dxe5TfM_7-W7Zs_wiXUjrXo0f4OY8PqBEKtPc0BTzGx8oDpZXiC_-zb5acq5NQX_yYdXyc5S91gkO5KJ3_BQXI7gqK1gmmSnnQm3kJV6TQdnmIjRb81axBs22OMTzmJ6iUAoedXdC-2L9DEl0EsMOavvVY_SdKstWB_tONm7445lJMlnbNERmWFrzuV66vonaNzwg95WMkyL31jYkGlE4lWvO7BsQIgp8EoXTIKCN86nii3EkRxWZ6Rnq3k0w5e8f64xYN7kGmpypCjWW2Dtg'
# token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IkFRQUJBQUFBQUFEWHpaM2lmci1HUmJEVDQ1ek5TRUZFWlBaR1YzYXFTcWM2czFtMXJsV3hsdWJBNjVkdXZtd1BOVEhlYkJ5VTNOb2RZZldyYmpnQmExT2tHXzNGT2pvakRfY0VhaV9tT1ZzU24zQUVVVlluc1NBQSIsImFsZyI6IlJTMjU2IiwieDV0IjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3Iiwia2lkIjoiN19adWYxdHZrd0x4WWFIUzNxNmxValVZSUd3In0.eyJhdWQiOiJodHRwczovL2dyYXBoLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNTMyMzk3MjU1LCJuYmYiOjE1MzIzOTcyNTUsImV4cCI6MTUzMjQwMTE1NSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFVUUF1LzhJQUFBQTlJWjNNemFaTGl0WXJtdWx6ZmFJNE95NS9POUlCa0d0YXVrN1pjR0NJRTJtbWpvbUluM2VCeGYxRUhxeTBvdG9wZDZqazZWMk1aUjBINkl0U1RqaERRPT0iLCJhbXIiOlsid2lhIiwibWZhIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIGV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkphaW4iLCJnaXZlbl9uYW1lIjoiU2hsb2FrIiwiaW5fY29ycCI6InRydWUiLCJpcGFkZHIiOiIxMzEuMTA3LjE1OS4xNzIiLCJuYW1lIjoiU2hsb2FrIEphaW4iLCJvaWQiOiI1ZWEyMGMyYS0zYTg3LTQxOWQtYTlkYy1mNzM5ZjI2YjBkZjciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMjEyNzUyMTE4NC0xNjA0MDEyOTIwLTE4ODc5Mjc1MjctMzE2ODIxMDkiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzAwMDBBQUJGRkUxOSIsInNjcCI6IkNhbGVuZGFycy5SZWFkV3JpdGUgQ29udGFjdHMuUmVhZFdyaXRlIERldmljZU1hbmFnZW1lbnRBcHBzLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRBcHBzLlJlYWRXcml0ZS5BbGwgRGV2aWNlTWFuYWdlbWVudENvbmZpZ3VyYXRpb24uUmVhZC5BbGwgRGV2aWNlTWFuYWdlbWVudENvbmZpZ3VyYXRpb24uUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50TWFuYWdlZERldmljZXMuUHJpdmlsZWdlZE9wZXJhdGlvbnMuQWxsIERldmljZU1hbmFnZW1lbnRNYW5hZ2VkRGV2aWNlcy5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50TWFuYWdlZERldmljZXMuUmVhZFdyaXRlLkFsbCBEZXZpY2VNYW5hZ2VtZW50UkJBQy5SZWFkLkFsbCBEZXZpY2VNYW5hZ2VtZW50UkJBQy5SZWFkV3JpdGUuQWxsIERldmljZU1hbmFnZW1lbnRTZXJ2aWNlQ29uZmlnLlJlYWQuQWxsIERldmljZU1hbmFnZW1lbnRTZXJ2aWNlQ29uZmlnLlJlYWRXcml0ZS5BbGwgRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRmlsZXMuUmVhZFdyaXRlLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIElkZW50aXR5Umlza0V2ZW50LlJlYWQuQWxsIE1haWwuUmVhZFdyaXRlIE1haWxib3hTZXR0aW5ncy5SZWFkV3JpdGUgTm90ZXMuUmVhZFdyaXRlLkFsbCBvcGVuaWQgUGVvcGxlLlJlYWQgcHJvZmlsZSBSZXBvcnRzLlJlYWQuQWxsIFNpdGVzLlJlYWRXcml0ZS5BbGwgVGFza3MuUmVhZFdyaXRlIFVzZXIuUmVhZEJhc2ljLkFsbCBVc2VyLlJlYWRXcml0ZSBVc2VyLlJlYWRXcml0ZS5BbGwgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJTcjZudVdDdU9jYkN1NzJ4WGNsXzNOdUZQeFhTYXNOSmVRVHdoYjY2SXZzIiwidGlkIjoiNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3IiwidW5pcXVlX25hbWUiOiJ0LXNoamFAbWljcm9zb2Z0LmNvbSIsInVwbiI6InQtc2hqYUBtaWNyb3NvZnQuY29tIiwidXRpIjoiMUJWUzg5Sk9zVUNwdDJQZVYxNERBQSIsInZlciI6IjEuMCIsInhtc19zdCI6eyJzdWIiOiJoU1JNQ3dzZ3hnSTFVeDNDTTAtR1Z0SDg5Q19Bbm5YWHZnMVBxMThqN3IwIn19.OShnVyrnnouBiNPI3HR7eVyI2PTxJ3d_88gZWnWt_UIw3T2KoDVihCBYke8nLcRYQUgZ1ns-YL-A1yAaYUw8P8WMBzwYiNV-Y-X8dXGnytv2t5F3pWnmX4zgnfKhKwfS3GlzKf5vysv5dwf2pyJeNU26tecrywnutKmOb5WMcD-gO0cb4v-etqH7e0958g68kXZ5BMjZ4FrxzpPD2n6cmdyh6pGRj3mtETNr-IJxUBWAiE9zsqnMbbyFJkB2dbZH7fCckTRC9Mxs5lNxVU_DWqudrehtnv6iu1tCoGXoCROLq2NK-x8uPO7PZH48kh7oc7Olkv0TxO7sNrBkyYBr3Q'
graph_endpoint = 'https://graph.microsoft.com/v1.0{0}'
app = Flask(__name__)
months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
          'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}


def make_api_call(method, url, token, payload=None, parameters=None):
    # Send these headers with all API calls
    headers = {'Authorization': 'Bearer {0}'.format(token),
               'Accept': 'application/json'}

    # Use these headers to instrument calls. Makes it easier
    # to correlate requests and responses in case of problems
    # and is a recommended best practice.
    request_id = str(uuid.uuid4())
    instrumentation = {'client-request-id': request_id,
                       'return-client-request-id': 'true'}

    headers.update(instrumentation)

    response = None

    if (method.upper() == 'GET'):
        response = requests.get(url, headers=headers, params=parameters)
    elif (method.upper() == 'DELETE'):
        response = requests.delete(url, headers=headers, params=parameters)
    elif (method.upper() == 'PATCH'):
        headers.update({'Content-Type': 'application/json'})
        response = requests.patch(
            url, headers=headers, data=json.dumps(payload), params=parameters)
    elif (method.upper() == 'POST'):
        headers.update({'Content-Type': 'application/json'})
        response = requests.post(url, headers=headers,
                                 data=json.dumps(payload), params=parameters)

    return response

# takes in python datetime object, returns all events within param: days
# retuns json with subject, location, details, start, end, attendees fields if you have accepted the event


def get_events(date, num_days=1):
    get_messages_url = graph_endpoint.format('/me/calendarview')

    start_date = date.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_date = (date + timedelta(days=num_days)).strftime('%Y-%m-%dT%H:%M:%SZ')
    query_parameters = {'startdatetime': start_date,
                        'enddatetime': end_date}

    r = make_api_call('GET', get_messages_url, token,
                      parameters=query_parameters)
    accepted_response = {'accepted', 'organizer'}

    if (r.status_code == requests.codes.ok):
        json_response = r.json()["value"]
        events = [{'subject': e['subject'], 'location': e['location']['displayName'], 'details': e['bodyPreview'], 'start': e['start']['dateTime'], 'end': e['end']['dateTime'],
                   "attendees": [{'name': a['emailAddress']['name']} for a in e['attendees']]} for e in json_response if e['responseStatus']['response'] in accepted_response]
        return json.dumps(events).encode('utf-8')
    else:
        return "{0}: {1}".format(r.status_code, r.text)


@skill_addevent.route('/add-event', methods=['POST'])
# takes in json body of intents
# does task at midnight on day of deadline for duration minutes
# add event to calendar
def skill_addevent_root(post_data):
    #   post_data = request.json
    if post_data['intent'] == 'add-task':
        subject, start, duration = None, None, None
        for e in post_data['entities']:
            if 'Calendar.Subject' in e:
                subject = e['Calendar.Subject']
            if 'builtin.datetimeV2.duration' in e:
                duration = int(
                    ''.join(filter(str.isdigit, str(e["builtin.datetimeV2.duration"]))))
            if "builtin.datetimeV2.date" in e:
                if 'min' in e["builtin.datetimeV2.date"]:
                    duration = int(
                        ''.join(filter(str.isdigit, str(e["builtin.datetimeV2.date"]))))
                else:
                    for month in months:
                        if month in e["builtin.datetimeV2.date"]:
                            start = datetime(2018, months[month], int(
                                ''.join(filter(str.isdigit, str(e["builtin.datetimeV2.date"])))))
        if subject and start and duration:
            #   print(subject, start, start + timedelta(minutes=duration))
            get_messages_url = graph_endpoint.format('/me/events')

            event = {"subject": subject, "start": {"dateTime": start.strftime('%Y-%m-%dT%H:%M:%S'), "timeZone": "Pacific Standard Time"}, "end": {
                "dateTime": (start + timedelta(minutes=duration)).strftime('%Y-%m-%dT%H:%M:%S'),
                "timeZone": "Pacific Standard Time"
            }}
            r = make_api_call('POST', get_messages_url, token, payload=event)
            if (r.status_code == requests.codes.ok):
                # resp = Response(json.dumps(
                    # {"txt-response": "Task successfully added!"}), status=200, mimetype='application/json')
                return render_template('skill_addevent.html', txt_response="Task successfully added!")
                # return
            else:
                print("{0}: {1}".format(r.status_code, r.text))
    return render_template('skill_addevent.html', txt_response="Failed to add task.")

    # resp = Response(json.dumps(
    #     {"txt-response": "Failed to add task."}), status=200, mimetype='application/json')
    # return resp


if __name__ == '__main__':
    app.run()
