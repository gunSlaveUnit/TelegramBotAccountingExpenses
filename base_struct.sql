create table category(
    id serial,
    name varchar(50) primary key,
    is_income boolean,
    aliases text
);

create table income(
    id serial,
    amount integer,
    created date,
    category_name varchar(50),
    clarification text,
    FOREIGN KEY(category_name) REFERENCES category(name)
);

create table expense(
    id serial,
    amount integer,
    created date,
    category_name varchar(50),
    clarification text,
    FOREIGN KEY(category_name) REFERENCES category(name)
);

insert into category (name, is_income, aliases)
values
    ('products', false, 'еда, продукты'),
    ('transport',  false, 'метро, автобус, metro, транспорт, taxi'),
    ('phone', false, 'связь, телефон'),
    ('books', false, 'литература, литра, лит-ра, книги'),
    ('internet', false, 'инет, inet, интернет'),
    ('subscriptions', false, 'подписка, подписки'),
    ('other', false, 'прочее');