_min = int(input("Enter the number of minutes:"))
sms = int(input("Enter the number of SMS:"))
print("Base amount:" + " " + "%.2f" % 15)
dop_min = 0
dop_sms = 0
if _min > 50:
    dop_min = "%.2f" % ((_min - 50) * 0.25)
    print("Additional amount for minutes:" + " " + dop_min)
if sms > 50:
    dop_sms = "%.2f" % ((sms - 50) * 0.15)
    print("Additional amount for sms:" + " " + dop_sms)
print("Call center tax:" + " " + str(0.44) +
      "\nGeneral tax:" + " " + str("%.2f" % ((float(dop_sms) + float(dop_min) + 15 + 0.44) * 0.05)) +
      "\nTotal:" + str(
    "%.2f" % (15 + 0.44 + float(dop_sms) + float(dop_min) + (float(dop_sms) + float(dop_min) + 15 + 0.44) * 0.05)))

# Evaluation: OK