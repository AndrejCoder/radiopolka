begin;
  alter table core_book add column file_format VARCHAR(10);
  alter table core_book add column file_size VARCHAR(10);

  update core_book set file_format = 'DJVU', file_size = '10,5' where id = 1;

  alter table core_book alter column file_format set not null;
  alter table core_book alter column file_size set not null;

commit;