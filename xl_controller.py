from openpyxl import Workbook, load_workbook
import ip_controller

def xl_populate(meraki_json, timestamp, workbook):
    #insert logging here

    block_list = ip_controller.get_block_list()
    
    site_json = meraki_json
    count = 2

    xl_sheet = workbook.active

    for i in site_json:
        meraki_dest = i["destination"]
        app = i["application"]
        protocol = i["protocol"]
        dest_port = i["port"]
        kilo_bytes_recv = i["recv"]
        kilo_bytes_sent = i["sent"]
        num_flows = i["flows"]
        active_time = i["activeTime"]
        num_client = i["numClients"]

        if meraki_dest == None:
            print("Destination is null, application type {0}.".format(app))
        else:
            if ip_controller.is_ip_or_hostname(meraki_dest) == "hostname":
                ip = ip_controller.convert_host_to_ip(meraki_dest)
                if ip in block_list:
                    active_blocklist = True

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

                    count = count + 1
                else:
                    active_blocklist = ip in block_list

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

                    count = count + 1

            elif ip_controller.is_private_ip(meraki_dest):
                print("Meraki destination {0} is a private address and will not be checked.".format(meraki_dest))
            else:
                if meraki_dest in block_list:
                    active_blocklist = True

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))

                    count = count + 1
                else:
                    active_blocklist = False

                    #insert logging here
                
                    xl_sheet["A{0}".format(str(count))] = meraki_dest
                    xl_sheet["B{0}".format(str(count))] = str(active_blocklist)
                    xl_sheet["C{0}".format(str(count))] = protocol
                    xl_sheet["D{0}".format(str(count))] = dest_port
                    xl_sheet["E{0}".format(str(count))] = kilo_bytes_recv
                    xl_sheet["F{0}".format(str(count))] = kilo_bytes_sent
                    xl_sheet["G{0}".format(str(count))] = num_flows
                    xl_sheet["H{0}".format(str(count))] = num_client
                    xl_sheet["H{0}".format(str(count))] = active_time

                    workbook.save(filename="dest_talos_blacklist_check_{0}.xlsx".format(timestamp))
                    #insert logging here

                    count = count + 1
            
    #insert logging here
    return "All Done!!!"
