curl http://127.0.0.1:5000/



curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{
  "UserId": 1,
  "Name": "Savit",
  "Package_Period": 90,
  "Start_Date": "2026-03-01",
  "Amount_Paid": 3000,
  "Phone_Number": "9876543210"
}'

curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{
  "UserId": 2,
  "Name": "Rahul",
  "Package_Period": 30,
  "Start_Date": "2026-03-10",
  "Amount_Paid": 1200,
  "Phone_Number": "9999999999"
}'

curl http://127.0.0.1:5000/users


curl http://127.0.0.1:5000/users/Savit

curl -X PUT http://127.0.0.1:5000/users/Savit \
-H "Content-Type: application/json" \
-d '{
  "Package_Period": 120,
  "Amount_Paid": 4000
}'

curl -X PUT http://127.0.0.1:5000/users/Savit \
-H "Content-Type: application/json" \
-d '{
  "Start_Date": "2026-04-01"
}'

curl -X DELETE http://127.0.0.1:5000/users/Savit