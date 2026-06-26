SELECT student_id, exam_id, score
FROM exam_results e1
WHERE exam_id = (
    SELECT exam_id 
    FROM exam_results e2
    WHERE e1.student_id = e2.student_id
    ORDER BY score DESC, exam_id ASC
    LIMIT 1
)
ORDER BY student_id;