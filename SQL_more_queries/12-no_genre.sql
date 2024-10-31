-- Seleccionar todas las series que no tienen un género asociado
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Asegúrate de usar el nombre correcto
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
