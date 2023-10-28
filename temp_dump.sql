-- Adminer 4.8.1 PostgreSQL 16.0 (Debian 16.0-1.pgdg120+1) dump

INSERT INTO "admins" ("id", "full_name", "tg_user_id") VALUES
(0,	'Шлюпкина Алла Ильинична',	167879922),
(1,	'Рома',	981197616);

INSERT INTO "homeworks" ("id", "group", "name_lesson", "text", "photos_name", "documents_name", "teacher_name", "made_date", "edit_date") VALUES
(1,	'ИС-23',	'Облачные технологии',	'Веник из березы',	'AgACAgIAAxkBAAINHWU7WTdZKVmAdQthBP7BfuEkm4CdAAJdzTEbb6_ZSV_JYEXHSwv3AQADAgADeQADMAQ AgACAgIAAxkBAAINHmU7WTcpO8P4WZYkiObFICGozprIAAJezTEbb6_ZSZxaOr2Ofu3rAQADAgADeQADMAQ AgACAgIAAxkBAAINH2U7WTeKIBqsz9V4-MDZJwiI1YqHAAJfzTEbb6_ZSblAZhP7xpK0AQADAgADeQADMAQ AgACAgIAAxkBAAINIGU7WTe8kkAOWmkXVk21xy70SoB7AAJgzTEbb6_ZSfT9-C-gofWPAQADAgADeQADMAQ',	'Нет файлов',	'Щипанкина  А.А.',	'2023-10-27',	'2023-10-27'),
(2,	'ИС-28',	'Операционные системы и среды',	'АБОБА',	'Нет фото',	'Нет файлов',	'Трищук С.А.',	'2023-10-27',	'2023-10-27');

INSERT INTO "students" ("id", "tg_user_id", "user_name", "group", "is_departament", "made_date") VALUES
(3,	1015326517,	'Софья Трищук',	'БУ-21',	'f',	'2023-10-27'),
(8,	2066274131,	'Дарья',	'ИС-11',	'f',	'2023-10-27'),
(9,	2002268318,	'Goose👉🍅👈',	'ИС-28',	'f',	'2023-10-27'),
(15,	1157932550,	'Погорелова Мария',	'ИС-13',	'f',	'2023-10-27'),
(16,	612364225,	'maksimka',	'БД-11',	'f',	'2023-10-27'),
(17,	1976945960,	'Что-то',	'ИС-22',	'f',	'2023-10-27'),
(18,	1094108028,	'Nikon Dvorfs',	'ИС-22',	'f',	'2023-10-27');

INSERT INTO "teachers" ("id", "tg_user_id", "user_name", "full_name", "is_departament", "made_date") VALUES
(5,	895297805,	'Relicter',	'Щипанкина  А.А.',	'f',	'2023-10-29');

INSERT INTO "teachers_data" ("id", "password", "full_name", "made_date") VALUES
(2,	'0000',	'Трищук С.А.',	'2023-10-27'),
(3,	'0108',	'Щипанкина  А.А.',	'2023-10-27');

INSERT INTO "training_departament_data" ("id", "password", "made_date") VALUES
(0,	'0101',	NULL),
(1,	'8888',	'2023-10-27');

-- 2023-10-28 22:28:01.65043+00