import qrcode
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

while True:
  try:
    url = input('Enter url accurately: ').lower().replace(' ', '')
    file_name = input('Enter the file name you want to save it as: ').lower().replace(' ', '')

    if not url.startswith(('http://', 'https://')):
      print('Please enter a valid URL starting with http:// or https://')
      continue

    if not(file_name.endswith('.png')):
      file_name += '.png' 

    break

  except ValueError:
    print('Invalid Value')

qr_code = qrcode.make(url)
qr_code.save(os.path.join(script_dir, file_name))