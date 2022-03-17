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
--added 1 Distrubutor and 1 shop with name forthetest
--added 1000 Filme with gen forthetest and 1 sala with name forthetest
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

execute testing 2

select * from TestRunViews