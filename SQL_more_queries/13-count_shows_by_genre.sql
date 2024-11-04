SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM tv_genres g
JOIN tv_shows_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.show_id = s.id
GROUP BY g.name
HAVING COUNT(s.id) > 0
ORDER BY number_of_shows DESC;
