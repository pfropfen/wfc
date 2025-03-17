CREATE DATABASE IF NOT EXISTS maps;
USE maps;
CREATE TABLE IF NOT EXISTS mapchunks (
	mapID VARCHAR(36),
	chunkID VARCHAR(36),
	locationX INT,
	locationY INT,
	entropyTolerance INT,
	content JSON,
	computed BOOLEAN);

