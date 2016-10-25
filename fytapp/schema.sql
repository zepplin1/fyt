drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  username text not null,
  email text not null,
  pw_hash text not null
);

drop table if exists appointment;
create table appointment (
  who_id integer,
  whom_id integer
);


