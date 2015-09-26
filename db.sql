drop table if exists chants;
drop table if exists bots;
drop table if exists bots_history;
drop type if exists bot_action;

create table chants (
    id serial,
    title text not null,
    lyrics text,
    url text
);

create table bots (
    id serial,
    username text not null,
    is_main boolean
);

create type bot_action as enum (
    'add',
    'remove',
    'update'
);

create table bots_history (
    id serial,
    username text,
    action bot_action,
    revision serial
);

insert into bots (username, is_main)
values 
('fenerbahce_bot', True),
('fenerbahce_vote_bot', False),
('fenerbahce_photobot', False),
('fenerbahcebetsbot', False),
('fenetestbot', False),
('tahminetbot', False);

insert into bots_history (username, action)
values
('fenetestbot', 'add'),
('fenerbahcebetsbot', 'remove'),
('tahminetbot', 'update');

insert into chants (title, lyrics, url)
values 
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant1.mp3'),
('Aşığım Aşığım Sana', E'Aşığım aşığım sana\n'
    'Doyamıyorum ki sana\n'
    'Neyleyim ben bu dünyayı of of of\n'
    'Sen olmayınca Kanarya', 'http://fenegram.herokuapp.com/static/chant2.mp3'),
('Sevdamıza Kimse Engel Olamaz', E'Sevdamıza kimse engel olamaz\n'
    'Bazen hüzün vardır bazen mutluluk\n'
    'Fener sevgisinin adı konamaz\n'
    'Ne kupa büyüklüğü ne şampiyonluk!', 'http://fenegram.herokuapp.com/static/chant3.mp3'),
('Sensiz Hayat Bir İşkence', E'Sensiz hayat bir işkence\n'
    'Dilimdesin gündüz gece\n'
    'Satır satır, hece hece\n'
    'Şampiyonsun Fenerbahçe', 'http://fenegram.herokuapp.com/static/chant4.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant5.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant6.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant7.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant8.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant9.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant10.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant11.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant12.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant13.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant14.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant15.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant16.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant17.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant18.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant19.mp3'),
('Bir Tek Sana Tutuldu Bu Kalpler', E'Bir tek sana tutuldu bu kalpler\n'
    'Sevdanın uğruna tanımaz hiç engel\n'
    'Bizim için heves değilsin sen FENER\n'
    'Aşkın bize yeter!', 'http://fenegram.herokuapp.com/static/chant20.mp3');


