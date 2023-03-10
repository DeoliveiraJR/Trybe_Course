USE PiecesProviders;

-- Tabela Pieces
SELECT * FROM PiecesProviders.Pieces;

-- Tabela Providers
SELECT * FROM PiecesProviders.Providers;

-- Tabela Provides
SELECT * FROM PiecesProviders.Provides;

-- Escreva uma query para exibir a peça e o preço de tudo que é provido pela empresa RBT.
SELECT Piece, Price FROM Provides
WHERE Provider = 'RBT'; 

-- Escreva uma query para exibir todas as informações das cinco peças com os maiores preços.
SELECT Piece, Price FROM Provides
ORDER BY Price DESC
LIMIT 5;

-- Escreva uma query para exibir o nome das empresas e o preço das quatro peças com os maiores preços, começando a lista a partir do 3º item.
SELECT DISTINCT Provider, Price FROM Provides
ORDER BY Price DESC
LIMIT 4
OFFSET 2;

-- Escreva uma query para exibir todas as informações das peças que são providas pela empresa HAL. Ordene o resultado pelos preços das peças de forma decrescente.
SELECT * FROM Provides
WHERE Provider = 'HAL'
ORDER BY Price DESC;

-- Escreva uma query para exibir por quantas empresas a peça 1 é provida.
SELECT COUNT(Provider) FROM Provides
WHERE Piece = 1;