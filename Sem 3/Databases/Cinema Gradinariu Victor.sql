Create database Cinemav2
go
use Cinemav2
go

create table Departamente
(Did int primary key identity,
Nume varchar(50))

create table Manageri
(Mid int foreign key references Departamente(Did),
Nume varchar(50),
Salariu int,
CONSTRAINT pk_manageri PRIMARY KEY(Mid)
)

create table Filme
(Fid int primary key identity,
Nume varchar(50),
Gen varchar(50),
Data_lansare date
)

create table Magazine
(Maid int primary key identity,
Nume varchar(50)
)

create table Angajati
(Aid int primary key identity,
Nume varchar(50),
Salariu int,
Did int foreign key references Departamente(Did),
Maid int foreign key references Magazine(Maid)
)

create table Bilete
(Bid int primary key identity,
Pret int,
Fid int foreign key references Filme(Fid),
Maid int foreign key references Magazine(Maid)
)

create table Sali
(Said int primary key identity,
Nume varchar(50),
Capacitate int
)

create table SaliFilme
(Said int foreign key references Sali(Said),
Fid int foreign key references Filme(Fid),
constraint pk_SaliFilme primary key (Said,Fid)
)

create table Distribuitori
(Diid int primary key identity,
Nume varchar(50),
Telefon int,
Frecventa_cumparare varchar(50)
)

create table Produse
(Pid int primary key identity,
Nume varchar(50),
Pret int,
Diid int foreign key references Distribuitori(Diid),
Maid int foreign key references Magazine(Maid)
)

insert into Departamente (Nume) values
('Curatenie'),
('Sali'),
('Magazine');

select * from Departamente

insert into Manageri (Mid, Nume, Salariu) values
(1,'Goergeta Miahela', 3000),
(2,'Alex Butnar', 5000),
(3,'Tibi Alexu', 4000);

select * from Manageri

insert into Angajati (Nume,Salariu,Did) values
('Petrisor',1800,1),
('Lucaciu',1800,1),
('Popescu',1850,1),
('Johnson',2000,1),

('Marcus',2200,2),
('Peterson',2200,2),
('Jeb',2200,2),
('Petrisor',2200,2),

('Alexandra',2500,3),
('Monica',2300,3);

select * from Angajati

insert into Magazine (Nume) values
('Afara'),
('Inauntru');

update Angajati set Maid=1 where Aid=9;
update Angajati set Maid=2 where Aid=10;

select * from Angajati

insert into Filme (Nume,Gen,Data_lansare) values
('Kung Fu Panda','Family/Comedy','2008-07-04'),
('Matrix','Sci-fi/Action','1999-03-31'),
('Avatar','Sci-fi','2009-12-18'),
('Titanic','Romance/Drama','1997-12-17'),
('Forest Gump','Drama/Romance','1994-07-06'),
('The Avengers','Action/Adventure','2012-05-04'),
('Avengers: Infinity War','Action/Sci-fi','2018-04-23'),
('Avengers: Endgame','Action/Sci-fi','2019-04-26'),
('Lord Of The Rings Fellowship Of Ring','Fantasy/Adventure','2002-02-01'),
('Lord Of The Rings: The Two Towers','Fantasy/Adventure','2003-02-28'),
('Lord Of The Rings: Return Of The King','Fantasy/Adventure','2004-01-02');

select * from Filme

insert into Bilete (Pret,Fid,Maid) values
(10,1,1),
(15,2,1),
(25,3,1),
(15,5,1),
(25,6,1),
(30,7,1),
(30,8,1),
(20,9,1),
(20,10,1),
(20,11,1);

insert into Sali (Nume,Capacitate) values
('Low',30),
('Medium',60),
('High',100);

insert into SaliFilme(Fid,Said) values
(1,1),
(2,1),
(5,1),
(3,2),
(6,3),
(7,3),
(8,3),
(9,2),
(10,2),
(11,2);

insert into Distribuitori (Nume,Telefon,Frecventa_cumparare) values
('Metro',4457334,'2/saptamana'),
('Sc. Produsecinema',9345843,'2/luna');

insert into Produse (Nume,Pret,Diid,Maid) values
('Popcorn mic', 10, 1, 2),
('Popcorn mediu', 15, 1, 2),
('Popcorn mare', 20, 1, 2),
('Suc mic',3,1,2),
('Suc mediu',6,1,2),
('Suc mare',8,1,2),
('Nachos mic', 8, 1, 2),
('Nachos mediu', 14, 1, 2),
('Nachos mare', 18, 1, 2),
('Tricou',60,2,1),
('Sticker',5,2,1),
('Pantaloni',40,2,1),
('Geanta',80,2,1),
('Ghiozdan',70,2,1);

--1.Numele produselor vandute de alexandra cu pret mai maire de 50
--where,>2tabele,
select Produse.Nume
from ((Angajati 
inner join Magazine on Angajati.Maid = Magazine.Maid) 
inner join Produse on Produse.Maid = Magazine.Maid)
where Angajati.Nume = 'Alexandra' and Produse.Pret > 50


--2.In ce sali se difuzeaza filmele avengers
--where,>2tabele,n:m
select Sali.Nume as Sala
from ((Filme
inner join SaliFilme on SaliFilme.Fid = Filme.Fid)
inner join Sali on Salifilme.Said = Sali.Said)
where Filme.Nume like '%Avengers%'

--3.cate filme se difuzeaza in sala cea mai mare
--groupby,having,n:m,>2tabele
select COUNT(Sali.Nume) as cate
from ((Filme
inner join SaliFilme on SaliFilme.Fid = Filme.Fid)
inner join Sali on Salifilme.Said = Sali.Said)
group by Sali.Nume
having Sali.Nume like 'High'


--4.cate filme sunt din fiecare gen avand mai mult de o aparitie
--groupby having
select count(Gen) as Cate,Gen
from Filme
group by Gen
having count(Gen)>1


--5.cate produse se vand la fiecare magazin
--groupby
select count(Pid) as cate,Maid
from Produse
group by Maid


--6.ce salarii au angajatii de care are grija alex
--where,distinct,>2tabele
select distinct Angajati.Salariu
from ((Manageri
inner join Departamente on Manageri.Mid = Departamente.Did)
inner join Angajati on Departamente.Did = Angajati.Did)
where Manageri.Nume like '%Alex%'

--7.Ce produse Cumparam de la distibuitori cu pretul mai mare de 10
--where,>2tabele
select Distribuitori.Nume,Produse.Nume
from ((Distribuitori
inner join Produse on Produse.Diid = Distribuitori.Diid)
inner join Magazine on Produse.Maid = Magazine.Maid)
where Produse.Pret >10

--8.toate detallile despre produse,distribuitori si magazine
-->2tabele
select *
from ((Distribuitori
inner join Produse on Produse.Diid = Distribuitori.Diid)
inner join Magazine on Produse.Maid = Magazine.Maid)

--9.toate filmele si salile in care se difuzeaza
-->2tabele
select *
from ((Filme
inner join SaliFilme on SaliFilme.Fid = Filme.Fid)
inner join Sali on Salifilme.Said = Sali.Said)

--10.genurile de filme cu pretul mai mare egal de 20 lei
--distinct,where
select distinct Gen
from (Filme
inner join Bilete on Bilete.Fid = Filme.Fid)
where Bilete.Pret>20


create table Versiuni
(versionNumber int)

insert into Versiuni values (0)
go

--modifica tipul unei coloane - versiune1
create procedure V1 as
begin
	alter table Produse
	alter column Pret Bigint
	print 'Coloana Pret din produse a fost modificata'
end
go

--Reverse versiune1
create procedure RV1 as
begin
	alter table Produse
	alter column Pret int
	print 'Coloana Pret din produse a revenit la forma initiala'
end
go

--adauga o constrangere de valoare implicita pentru un camp - versiune2
create procedure V2 as
begin
	alter table Bilete
	add constraint df_p default 10 for Pret
	print 'Coloana pret din bilete a devenit 10 by default'
end
go

--reverse versiune2
create procedure RV2 as
begin
	alter table Bilete
	drop constraint df_p
	print 'Coloana pret nu mai are constrangere implicita'
end
go

--creeaza o tabela - versiune3
create procedure V3 as
begin
	create table Test(
	tid int not null primary key,
	nota int);
	print 'A fost creeata tabela Test'
end
go

--reverse versiune3
create procedure RV3 as
begin
	drop table Test
	print 'A fost stersa tabela Test'
end
go

--adauga un camp nou - versiune4
create procedure V4 as
begin
	alter table Angajati
	add Fericire int
	print 'A fost adaugata coloana fericire in Angajati'
end
go

--reverse versiune4
create procedure RV4 as
begin
	alter table Angajati
	drop column Fericire
	print 'A fost stearsa coloana fericire din Angajati'
end
go

--creeaza o  constrangere de cheie straina - versiune5
create procedure V5 as
begin
	alter table Sali
	add Mid int
	alter table Sali
	add constraint fk_Sali foreign key(Mid) references Manageri(Mid)
	print 'A fost adaugata constrangerea de cheie straina in sali'
end
go

--reverse versiune5
create procedure RV5 as
begin
	alter table Sali
	drop constraint fk_Sali
	alter table Sali
	drop column Mid
	print 'A fost stearsa constrangerea de cheie straina in sali'
end
go

create procedure main
@versiune int
as begin
	if @versiune < 0 or @versiune > 5
	begin
		print 'Nu exista aceasta versiune'
		return
	end

	declare @versiuneCurenta int
	select @versiuneCurenta = Versiuni.versionNumber from Versiuni
	if @versiune = @versiuneCurenta
	begin
		print 'Suntem deja la aceasta versiune'
		return
	end

	declare @procedura varchar(5)
	while @versiuneCurenta < @versiune
	begin
		set @versiuneCurenta = @versiuneCurenta + 1
		set @procedura = 'V'+ CONVERT(varchar(1),@versiuneCurenta)
		exec(@procedura)
		update Versiuni set versionNumber = @versiuneCurenta
		print 'Am crescut la versiunea ' +CONVERT(varchar(1),@versiuneCurenta)
	end

	while @versiuneCurenta > @versiune
	begin
		set @procedura = 'RV'+ CONVERT(varchar(1),@versiuneCurenta)
		set @versiuneCurenta = @versiuneCurenta - 1
		exec(@procedura)
		update Versiuni set versionNumber = @versiuneCurenta
		print 'Am scazut la versiunea ' +CONVERT(varchar(1),@versiuneCurenta)
	end
end
go
		
select * from Versiuni
UPDATE Versiuni SET versionNumber = 0

exec main 5


insert into Tables (Name) values
('Distribuitori'),
('Produse'),
('SaliFilme')

select * from Tables

CREATE VIEW View_1 AS
	SELECT * from Distribuitori
GO

CREATE VIEW View_2 AS
	SELECT p.Nume as 'Nume Produs', p.Pret, m.Nume as 'Nume Magazin'
	FROM Produse p INNER JOIN Magazine m ON p.Maid = m.Maid
GO

CREATE VIEW View_3 AS
	select COUNT(Sali.Nume) as 'Nr filme'
	from SaliFilme inner join Sali on Salifilme.Said = Sali.Said
	group by Sali.Nume
GO


insert into Views (Name) values
('View_1'),
('View_2'),
('View_3')

select * from Views

insert into Tests (Name) values 
('delete_table'),
('insert_table'),
('select_view')

select * from Tests

insert into TestViews (TestID,ViewID) values 
(3,1),
(3,2),
(3,3)

select * from TestViews

insert into TestTables (TestID,TableID,NoOfRows,Position) values
(1,1,1000,3),
(1,2,1000,2),
(1,3,1000,1),
(2,1,1000,1),
(2,2,1000,2),
(2,3,1000,3)

select * from Tables
go

create procedure delete1 as
begin
	delete from Distribuitori where Telefon = 4342
end
go

create procedure delete2 as
begin
	delete from Produse where Pret = 9999
end
go

create procedure delete3 as
begin
	DECLARE @NoOfRows int
	DECLARE @n int
	DECLARE @sai int
	DECLARE @fii int

	SELECT TOP 1 @sai = Said from Sali where Sali.Nume = 'forthetest'
	SELECT TOP 1 @NoOfRows = NoOfRows FROM TestTables WHERE TestTables.TableID = 3 AND TestTables.TestID = 2
	SET @n=1

	SELECT @fii = Min(Fid) From Filme where Filme.Gen = 'forthetest' --first id of already inserted movies

	WHILE @n<@NoOfRows
	BEGIN
		delete from SaliFilme where SaliFilme.Fid = @fii and SaliFilme.Said = @sai
		set @fii=@fii+1
		SET @n=@n+1
	END
end
go

create procedure insert1 as
begin
	DECLARE @NoOfRows int
	DECLARE @n int
	DECLARE @t VARCHAR(30)

	SELECT TOP 1 @NoOfRows = NoOfRows FROM TestTables WHERE TestTables.TableID = 1 AND TestTables.TestID = 2
	SET @n=1

	WHILE @n<@NoOfRows
	BEGIN
		SET @t = 'DistTest' + CONVERT (VARCHAR(5), @n)
		INSERT INTO Distribuitori(Nume, Telefon, Frecventa_cumparare) VALUES (@t,4342, '10/10')
		SET @n=@n+1
	END
end
go

create procedure insert2 as
begin
-- Have to have 1 Distribuitor and 1 magazin with name forthetest prior 
	DECLARE @NoOfRows int
	DECLARE @n int
	DECLARE @t VARCHAR(30)
	Declare @fk1 int
	Declare @fk2 int
	SELECT TOP 1 @fk1 = Diid FROM Distribuitori WHERE Distribuitori.Nume = 'forthetest'
	SELECT TOP 1 @fk2 = Maid FROM Magazine WHERE Magazine.Nume = 'forthetest'

	SELECT TOP 1 @NoOfRows = NoOfRows FROM TestTables WHERE TestTables.TableID = 2 AND TestTables.TestID = 2
	SET @n=1

	WHILE @n<@NoOfRows
	BEGIN
		SET @t = 'ProdTest' + CONVERT (VARCHAR(5), @n)
		INSERT INTO Produse(Nume, Pret,Diid,Maid) VALUES (@t,9999,@fk1,@fk2)
		SET @n=@n+1
	END
end
go

create procedure insert3 as
begin
--have to have 1000 Filme added prior and 1 sala with name forthetest
	DECLARE @NoOfRows int
	DECLARE @n int
	DECLARE @sai int
	DECLARE @fii int

	SELECT TOP 1 @sai = Said from Sali where Sali.Nume = 'forthetest'
	SELECT TOP 1 @NoOfRows = NoOfRows FROM TestTables WHERE TestTables.TableID = 3 AND TestTables.TestID = 2
	SET @n=1

	SELECT @fii = Min(Fid) From Filme where Filme.Gen = 'forthetest' --first id of already inserted movies

	WHILE @n<@NoOfRows
	BEGIN
		INSERT INTO SaliFilme(Fid,Said) values(@fii,@sai)
		set @fii=@fii+1
		SET @n=@n+1
	END
end
go

create procedure view1 as
begin
	select * from View_1
end
go

create procedure view2 as
begin
	select * from View_2
end
go

create procedure view3 as
begin
	select * from View_3
end
go

create procedure AddN as
begin
--have to have 1 Distrubutor and 1 shop with name forthetest prior 
--have to have 1000 Filme with gen forthetest added prior and 1 sala with name forthetest
	DECLARE @NoOfFilme int
	DECLARE @n int
	DECLARE @t VARCHAR(30)

	SELECT TOP 1 @NoOfFilme = NoOfRows FROM TestTables WHERE TestTables.TableID = 3 AND TestTables.TestID = 2
	SET @n=1 -- first we have no row inserted

	WHILE @n<@NoOfFilme
	BEGIN
		-- we must set a unique value for the primary key 
		-- we should insert a different value for the other fields
		SET @t = 'FilmeTest' + CONVERT (VARCHAR(5), @n)

		INSERT INTO Filme(Nume, Gen, Data_lansare) VALUES (@t,'forthetest','1911-11-11')
		SET @n=@n+1
	END

	insert into Sali (Nume,Capacitate) values ('forthetest',100)
	insert into Distribuitori(Nume) values ('forthetest')
	insert into Magazine(Nume) values ('forthetest')
end
go

execute AddN

create procedure testing
@nrtest int
as begin
	if @nrtest < 0 or @nrtest > 3
	begin
		print 'Nu exista acest test'
		return
	end


	DECLARE @ds DATETIME -- start time test
	DECLARE @di DATETIME -- intermediate time test
	DECLARE @de DATETIME -- end time test
	declare @ins varchar(10)
	declare @del varchar(10)
	declare @vie varchar(10)
	set @ins = 'insert' + CONVERT(varchar(1),@nrtest)
	set @del = 'delete' + CONVERT(varchar(1),@nrtest)
	set @vie = 'view' + CONVERT(varchar(1),@nrtest)
	
	SET @ds = GETDATE()
	
	execute @del
	execute @ins
	
	SET @di=GETDATE()
	execute @vie
	SET @de=GETDATE()

	Declare @desc varchar(50)
	Set @desc = 'Testare pentru ' + CONVERT(varchar(1),@nrtest)
	Insert into TestRuns (Description,StartAt,EndAt) values (@desc,@ds,@de)
	-- extract the TestRunId and “combine” it with the Id of table involved and also with the view involved in the corresponding tables
	declare @idtest int
	SELECT @idtest = Max(TestRunId) From TestRuns
	Insert into TestRunTables(TestRunId, TableID,StartAt,EndAt) values (@idtest, @nrtest, @ds, @di)
	Insert into TestRunViews(TestRunID,ViewID,StartAt,EndAt)values (@idtest,@nrtest,@di,@de)

end
go

execute testing 3

select * from TestRuns
select * from TestRunTables
select * from TestRunViews