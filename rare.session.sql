-- WHERE EXISTS (SELECT * FROM users WHERE email = 'chugg.butt@email.com' AND password = 'password') THEN SELECT 'true' ELSE SELECT 'false' 
-- SELECT * FROM users
SELECT EXISTS ( SELECT * FROM users WHERE email = 'chugg.buttt@email.com' AND password = 'password')
