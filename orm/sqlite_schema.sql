create table hex_colors (id integer primary key autoincrement, hexvalue text);
-- All Colors (White)
insert into hex_colors (hexvalue) values ('FFFFFF');
-- No Color (Black)
insert into hex_colors (hexvalue) values ('000000');
-- Reds
insert into hex_colors (hexvalue) values ('FF0000');
insert into hex_colors (hexvalue) values ('8E2323');
insert into hex_colors (hexvalue) values ('EE2C2C');
insert into hex_colors (hexvalue) values ('8C1717');
insert into hex_colors (hexvalue) values ('EE0000');
insert into hex_colors (hexvalue) values ('E3170D');
insert into hex_colors (hexvalue) values ('FC1501');
-- Oranges
insert into hex_colors (hexvalue) values ('E04006');
insert into hex_colors (hexvalue) values ('EE4000');
insert into hex_colors (hexvalue) values ('FF7F24');
insert into hex_colors (hexvalue) values ('FF6103');
insert into hex_colors (hexvalue) values ('EE8833');
insert into hex_colors (hexvalue) values ('FF4500');
insert into hex_colors (hexvalue) values ('FF6600');
-- Yellows
insert into hex_colors (hexvalue) values ('0000FF');
insert into hex_colors (hexvalue) values ('EEAD0E');
insert into hex_colors (hexvalue) values ('CDAB2D');
insert into hex_colors (hexvalue) values ('FFCC11');
insert into hex_colors (hexvalue) values ('FFC125');
insert into hex_colors (hexvalue) values ('FCDC3B');
insert into hex_colors (hexvalue) values ('FFD700');
-- Greens
insert into hex_colors (hexvalue) values ('00FF00');
insert into hex_colors (hexvalue) values ('7FFF00');
insert into hex_colors (hexvalue) values ('3F6826');
insert into hex_colors (hexvalue) values ('55AE3A');
insert into hex_colors (hexvalue) values ('228B22');
insert into hex_colors (hexvalue) values ('0AC92B');
insert into hex_colors (hexvalue) values ('43CD80');
-- Blues
insert into hex_colors (hexvalue) values ('0000FF');
insert into hex_colors (hexvalue) values ('388E8E');
insert into hex_colors (hexvalue) values ('37FDFC');
insert into hex_colors (hexvalue) values ('0D4F8B');
insert into hex_colors (hexvalue) values ('5D7B93');
insert into hex_colors (hexvalue) values ('0276FD');
insert into hex_colors (hexvalue) values ('000080');
-- Purples
insert into hex_colors (hexvalue) values ('7F00FF');
insert into hex_colors (hexvalue) values ('2E0854');
insert into hex_colors (hexvalue) values ('A020F0');
insert into hex_colors (hexvalue) values ('68228B');
insert into hex_colors (hexvalue) values ('9932CC');
insert into hex_colors (hexvalue) values ('AA00FF');
insert into hex_colors (hexvalue) values ('CC99CC');
-- Pinks
insert into hex_colors (hexvalue) values ('FF33CC');
insert into hex_colors (hexvalue) values ('FF1CAE');
insert into hex_colors (hexvalue) values ('CD1076');
insert into hex_colors (hexvalue) values ('FF00AA');
insert into hex_colors (hexvalue) values ('FF6EB4');
insert into hex_colors (hexvalue) values ('FF0066');
insert into hex_colors (hexvalue) values ('CD6889');

create table color_families (id integer primary key autoincrement, name text);
insert into color_families (name) values ('white');
insert into color_families (name) values ('black');
insert into color_families (name) values ('red');
insert into color_families (name) values ('orange');
insert into color_families (name) values ('yellow');
insert into color_families (name) values ('green');
insert into color_families (name) values ('blue');
insert into color_families (name) values ('purple');
insert into color_families (name) values ('pink');
