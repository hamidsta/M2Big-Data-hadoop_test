db.movies.find({},{title:1,_id:0})
db.movies.find({year:{$gt:2000,$lt:2019}},{title:1,_id:0})
db.movies.findOne({title:"Spider-Man"},{summary:1,_id:0})
db.movies.findOne({title:"Gladiator"},{director:1,_id:0})
db.movies.find({"actors.first_name":"Kirsten","actors.last_name":"Dunst"},{title:1,_id:0})
db.movies.count({summary:{$ne:null}})
db.movies.find({"actors.first_name":/^Cl/})
db.movies.find({$nor:[{genre:"drama"},{genre:"comedies"}]})
db.movies.find({},{title:1,actors:1,_id:0})
db.movies.find({"actors.first_name":"Clint","actors.last_name":"Eastwood","director.first_name":{$ne:"Clint"},"director.last_name":{$ne:"Eastwood"}})




db.movies_ex8.find({},{title:1,_id:0})
db.movies_ex8.find({year:{$gt:2000,$lt:2019}},{title:1,_id:0})
db.movies_ex8.findOne({title:"Spider-Man"},{summary:1,_id:0})
db.movies_ex8.aggregate({$lookup:{from:"artists",localField:"director._id",foreignField:"_id",as:"director"}},{$match:{title:"Gladiator"}},{$project:{_id:0,director:1}})
db.movies_ex8.aggregate({$lookup:{from:"artists",localField:"actors._id",foreignField:"_id",as:"actors"}},{$match:{"actors.first_name":"Kirsten","actors.last_name":"Dunst"}},{$project:{_id:0,title:1}})
db.movies_ex8.count({summary:{$ne:null}})
db.movies_ex8.aggregate({$lookup:{from:"artists",localField:"actors._id",foreignField:"_id",as:"actors"}},{$match:{"actors.first_name":/^Cl/}})
db.movies_ex8.find({$nor:[{genre:"drama"},{genre:"comedies"}]})
db.movies_ex8.aggregate({$lookup:{from:"artists",localField:"actors._id",foreignField:"_id",as:"actors"}},{$project:{_id:0,actors:1,title:1}})
db.movies_ex8.aggregate([{$lookup:{from:"artists",localField:"actors._id",foreignField:"_id",as:"actors"}},{$lookup:{from:"artists",localField:"director._id",foreignField:"_id",as:"director"}},{$match:{"actors.first_name":"Clint","actors.last_name":"Eastwood","director.first_name":{$ne:"Clint"},"director.last_name":{$ne:"Eastwood"}}}])
