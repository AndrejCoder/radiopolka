begin;

update core_book set id=5 where id=9;

ALTER SEQUENCE core_book_id_seq RESTART WITH 6;

commit;