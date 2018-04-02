begin;

update core_book set id=5 where id=9;

ALTER SEQUENCE core_book_pkey RESTART WITH 10000;

commit;