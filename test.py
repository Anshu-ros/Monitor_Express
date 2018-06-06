import trackingmore
import pprint
p = pprint.PrettyPrinter()
trackingmore.set_api_key('32de660c-b478-40f1-8c75-d5ada104be82')
var1 = trackingmore.create_tracking_data('delhivery','379211877610')
s = trackingmore.realtime_tracking(var1)
p.pprint(s)