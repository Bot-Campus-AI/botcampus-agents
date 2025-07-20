def grade_answer(answer):
    # Dummy scoring logic for now
    length_score = min(len(answer.split()), 100) / 100 * 5
    keyword_score = sum(1 for word in ["data", "analysis", "model", "AI"] if word in answer.lower())
    total_score = min(5, length_score + keyword_score)
    return round(total_score, 2)

def compare_answers(answer_dict):
    graded = {
        model: {
            "answer": ans,
            "score": grade_answer(ans)
        }
        for model, ans in answer_dict.items()
    }
    sorted_models = sorted(graded.items(), key=lambda x: x[1]["score"], reverse=True)
    return graded, sorted_models
