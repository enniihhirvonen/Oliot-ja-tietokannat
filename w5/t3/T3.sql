SELECT
artist.name AS name,
SUM(album.tracks) AS total_tracks
FROM artist
JOIN album
ON artist.id = album.artist_id
GROUP BY artist.name
ORDER BY
artist.name ASC;