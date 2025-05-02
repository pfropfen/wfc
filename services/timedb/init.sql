CREATE DATABASE IF NOT EXISTS times;
USE times;
CREATE TABLE IF NOT EXISTS mapTimes (
	mapID VARCHAR(36),
	mapSize INT,
	chunkCount INT,
	numberOfWorkers INT,
	startTime TIMESTAMP,
	endTime TIMESTAMP,
	totalDuration INT,
	PRIMARY KEY (mapID)
	);
	
CREATE TABLE IF NOT EXISTS chunkTimes (
	mapID VARCHAR(36),
	chunkID VARCHAR(36),
	startTime TIMESTAMP,
	endTime TIMESTAMP,
	chunkDuration INT,	
	PRIMARY KEY (mapID, chunkID),
	FOREIGN KEY (mapID) REFERENCES mapTimes(mapID)
	);