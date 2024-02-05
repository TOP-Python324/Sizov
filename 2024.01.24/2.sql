drop database if exists mus_library;
create database mus_library;
use mus_library;

create table styles (
    id smallint unsigned primary key auto_increment,
    title varchar(100) not null
);

create table publishers (
    id tinyint unsigned primary key auto_increment,
    name varchar(150) not null,
    coutry varchar(50) not null
);

create table performers (
    id smallint unsigned primary key auto_increment,
    name varchar(100) not null
);

create table music_collection (
    id smallint unsigned primary key auto_increment,
    name varchar(150) not null,
    release_date date,
    performers_id smallint unsigned not null
      references performers (id),
    styles_id smallint unsigned not null
      references styles (id),
    publishers_id smallint unsigned not null
      references publishers (id)
);

create table songs (
    id smallint unsigned primary key auto_increment,
    title varchar(200) not null,
    performers_id smallint unsigned not null
      references performers (id),
    styles_id smallint unsigned not null
      references styles (id),
    duration time,
    collection_id smallint unsigned not null
      references music_collection (id)
);

create table performers_collection (
    performers_id smallint unsigned not null
      references performers (id),
    collection_id smallint unsigned not null
      references music_collection (id),
    primary key (performers_id, collection_id)  
);

create table songs_collection (
    song_id smallint unsigned not null
      references songs (id),
    collection_id smallint unsigned not null
      references music_collection (id),
    primary key (song_id, collection_id)  
);