################
#�Ǻǣ��������˽�ע��
#��һ�����������ĳ���
################
contact = {}
contact_list = []
while 1:
    contact['name'] = raw_input("please input name: ")
    contact['phone'] = raw_input("please input phone number: ")
    contact_list.append(contact.copy())
    go_on = raw_input("continue?\n")
    if go_on == "yes":
        pass
    elif go_on == "no":
        break
    else:
        print "you didn't say no\n"
i = 1
for contact in contact_list:
    print "%d: name=%s" % (i, contact['name'])
    print "%d: phone=%s" % (i, contact['phone'])
    i = i + 1
