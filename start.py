from pgeocode import GeoDistance
import cgi
import pgeocode

dist = pgeocode.GeoDistance('GB')
calc_distance = int(dist.query_postal_code('SW1W 0NY', 'PO16 7GZ'))



print(calc_distance, "km")



form = cgi.FieldStorage()

code_1 = form.getvalue("input-1")
code_2 = form.getvalue("input-2")
print(code_1)