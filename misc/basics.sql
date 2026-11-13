SELECT DISTINCT group_name
FROM participants;

SELECT *
FROM participants
WHERE response IS NULL;

SELECT participant_id, age
FROM participants
ORDER BY age DESC
LIMIT 3;

-- exercise 03

--- part a

SELECT *
FROM participants
WHERE age >= 30 AND response IS NOT NULL AND group_name = 'treatment';

-- part b

SELECT *
FROM participants
WHERE participant_id IN (101, 103, 105);

SELECT *
FROM participants
WHERE participant_id = 101 OR participant_id = 103 OR participant_id = 105;

-- part c

--- 1 :UNKOWN
--- 2: FALSE
--- 3: TRUE
--- 4: UNKNOWN
--- 5: UNKOWN -- so, basically once we put not in front, we make it logical (truthy? i suppose we just treat it as truthy, but what we return is a logical object)
--- 6: UNKNOWN


-- part d

--- 1: it will return nothing, because it is UNKNOWN whether the participant is not in NULL

-- part e

SELECT participant_id, group_name, response
FROM participants
WHERE response IS NULL OR (group_name = 'treatment' and reponse > 0.8);

-- exercise 04

--- part a

SELECT p.participant_id, p.age, v.day, v.response
FROM participants AS p
INNER JOIN visits AS v
  ON p.participant_id = v.participant_id
WHERE group_name = 'treatment';

--- part b

SELECT p.participant_id, p.group_name, v.day, v.response
FROM participants AS p
LEFT JOIN visits AS V
  ON p.participant_id = v.participant_id; 

---- will have NULL, I think, for day and response for pid 104

--- part c

---- 1: 6 (however many rows are in visits)

---- 2: 7 (multiple rows for matches, one row for 104)

---- 3: 6 (keep all visits, add nothing as one row/pid in participants)

--- part d

---- 1: not sure, I think this depends on how sql wants to interpret an inner join. Sensibly, I think it returns multiple rows/pid. 2. see 1. 3. well, I guess it is more than one per pid. I'm thinking you could do SELECT DISCTIN p.participant_id.

--- part e

----- ovciously wrong, multipel reows/pid