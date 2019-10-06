from firebase import firebase
import json
import functions as f


# fire = firebase.FirebaseApplication('https://proj1-6f30a.firebaseio.com/',None)
#
#
# data = fire.get("/macs",None)
# # print(data)
#
# test_point = dict()
# test_point["macs"] = data

test_point = '''
    {
        "id": "21",
        "x": "-0.90",
        "y": "18",
        "macs": [
            {
                "name": "RehabLab",
                "value": [
                    -75,
                    -74,
                    -74,
                    -74,
                    -73,
                    -73,
                    -73,
                    -72,
                    -72,
                    -72,
                    -71,
                    -71,
                    -71,
                    -71,
                    -71,
                    -71,
                    -70,
                    -70,
                    -69,
                    -69
                ]
            },
            {
                "name": "STUDBME2",
                "value": [
                    -63,
                    -61,
                    -60,
                    -60,
                    -59,
                    -58,
                    -57,
                    -57,
                    -56,
                    -56,
                    -56,
                    -53,
                    -52,
                    -51,
                    -51,
                    -50,
                    -49,
                    -49,
                    -47
                ]
            },
            {
                "name": "CMP_LAB1",
                "value": [
                    -80,
                    -79,
                    -79,
                    -79,
                    -77,
                    -77,
                    -76,
                    -76,
                    -75,
                    -74,
                    -74,
                    -74,
                    -73,
                    -72,
                    -72,
                    -72,
                    -72,
                    -72,
                    -70
                ]
            }
        ]
    }
    '''

test_point = json.loads(test_point)

t_point = f.cal_avg_std(test_point)

print("****")
print(t_point)

ref_points = json.loads(open("data_points.json").read())

for point in ref_points:
    f.cal_avg_std(point)

# print("**avg-std**")
# for p in ref_points:
#     print(p)

points = f.improved_euclidean_dis(t_point,ref_points)

# print("****")
# for p in points:
#     print(p)

least_closest_points = f.sort_by_euclidean_dis(points)

print("**least_closest_points**")
for p in least_closest_points:
    print(p)

co_ordinates1 = f.get_position_acc_to_closest_points(least_closest_points)

print("**x1,y1 **")
for co_ord in co_ordinates1:
    print(co_ord)

po_ints = f.improved_joint_prop(t_point,ref_points)

# print("****")
# for p in po_ints:
#     print(p)

largest_closest_points = f.sort_by_joint_prob(po_ints)

print("** largest_closest_points **")
for p in largest_closest_points:
    print(p)

co_ordinates2 = f.get_position_x2_y2(largest_closest_points)

print("**x2,y2 **")
for co_ord in co_ordinates2:
    print(co_ord)

print("**x,y **")
co_ordinates = f.get_x_y(least_closest_points,largest_closest_points,co_ordinates1,co_ordinates2)
print(co_ordinates2)



# fire = firebase.FirebaseApplication('https://proj1-6f30a.firebaseio.com/',None)
# fire.put("/result/-LqDjLUpdJJvmYmxhwjN",'x',str(result['x']))
# fire.put("/result/-LqDjLUpdJJvmYmxhwjN",'y',str(result['y']))
# fire.put("/",'macs',ref_points[7]['macs'])



