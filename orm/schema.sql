create table hex_colors (id integer primary key autoincrement, hexvalue unique varchar);
-- All Colors
insert into colors (hexvalue) values ('FFFFFF');
-- No Color
insert into colors (hexvalue) values ('000000');
-- Blue
insert into colors (hexvalue) values ('0000FF');
-- Red
insert into colors (hexvalue) values ('FF0000');
-- Green
insert into colors (hexvalue) values ('00FF00');
-- Pink
insert into colors (hexvalue) values ('FF33CC');

create table color_families (id integer primary key autoincrement, name unique varchar);
insert into color_families (name) values ('white');
insert into color_families (name) values ('black');
insert into color_families (name) values ('blue');
insert into color_families (name) values ('red');
insert into color_families (name) values ('green');
insert into color_families (name) values ('pink');
insert into color_families (name) values ('yellow');
