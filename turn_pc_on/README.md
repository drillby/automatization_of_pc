### Wake on LAN:
* It is nessesary to enable WoL function in your BIOS and OS settings.
* File is in the turn_on_pc folder.
* You need to provide wol_adresses.json file with your broadcast IP and MAC addresses, formated like this:
```json
{
    "broadcast_ip": "ip",
    "macs": {
        "name": "mac"
    }
}
```
For reference you can see wol_adresses.json in this folder.

### Face recognition:
* Only usable on Linux machines.
* You need to update turn_on_pc/wol_adresses.json based on your mac address and broadcast IP.
* Also you need to provide your pictures to the turn_on_pc/images folder.
* Run by running the main.py file in turn_pc_on folder.
* You need to provide faces.json file with relative path to img and name of person on the img, formated like this:
```json
{
    "path": ["path1", "path2"],
    "name": ["person1", "person2"]
}
```
For reference you can see faces.json in this folder.
