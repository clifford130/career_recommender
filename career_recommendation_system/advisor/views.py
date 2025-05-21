# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .knowledge.rule_engine import get_recommendation
# from .knowledge.semantic_network import find_related_careers
# from .knowledge.ontology import load_career_ontology, query_career_requirements
# from .knowledge.nlp_module import extract_keywords

# def career_recommendation(request):
#     if request.method == 'POST':
#         # Retrieve form data: free-text input and comma-separated lists.
#         skills = request.POST.get('skills', '')
#         education = request.POST.get('education', '')
#         interests = request.POST.get('interests', '')
#         description = request.POST.get('description', '')  # free-text description

#         # Use NLP to extract additional keywords from the description.
#         nlp_keywords = extract_keywords(description)

#         profile_data = {
#             'skills': [skill.strip() for skill in skills.split(',') if skill.strip()] + nlp_keywords,
#             'education': education.strip(),
#             'interests': [interest.strip() for interest in interests.split(',') if interest.strip()]
#         }

#         # Rule-based recommendation
#         recommendation = get_recommendation(profile_data)

#         # Related careers using semantic network
#         related = []
#         for skill in profile_data['skills']:
#             related.extend(find_related_careers(skill))
#         related = list(set(related))

#         # Ontology query for additional career requirements
#         ontology_results = []
#         if recommendation:
#             g = load_career_ontology()  # Loads career.owl file (ensure it exists)
#             ontology_results = query_career_requirements(g, recommendation.replace(" ", ""))
        
#         context = {
#             'recommendation': recommendation,
#             'related_careers': related,
#             'ontology_info': ontology_results,
#             'nlp_keywords': nlp_keywords,
#         }
#         return render(request, 'advisor/recommendations.html', context)

#     return render(request, 'advisor/recommendations.html')
from django.shortcuts import render
from .knowledge.rule_engine import get_recommendation
from .knowledge.semantic_network import find_related_careers
from .knowledge.ontology import load_career_ontology, query_career_requirements
from .knowledge.nlp_module import extract_keywords
from .knowledge.ai_analysis import analyze_career_fit

def career_recommendation(request):
    if request.method == 'POST':
        # Retrieve form data
        skills = request.POST.get('skills', '')
        education = request.POST.get('education', '')
        interests = request.POST.get('interests', '')
        description = request.POST.get('description', '')  # free-text description

        # Use NLP to extract additional keywords from the description
        nlp_keywords = extract_keywords(description)

        profile_data = {
            'skills': [skill.strip() for skill in skills.split(',') if skill.strip()] + nlp_keywords,
            'education': education.strip(),
            'interests': [interest.strip() for interest in interests.split(',') if interest.strip()]
        }

        # Rule-based recommendation
        recommendation = get_recommendation(profile_data)

        # Advanced AI analysis of the free-text description
        ai_label, ai_score = analyze_career_fit(description)

        # Related careers using semantic network
        related = []
        for skill in profile_data['skills']:
            related.extend(find_related_careers(skill))
        related = list(set(related))

        # Ontology query for additional career requirements
        ontology_results = []
        if recommendation:
            g = load_career_ontology()  # Loads career.owl file (ensure it exists)
            ontology_results = query_career_requirements(g, recommendation.replace(" ", ""))
        
        context = {
            'recommendation': recommendation,
            'related_careers': related,
            'ontology_info': ontology_results,
            'nlp_keywords': nlp_keywords,
            'ai_analysis': {"label": ai_label, "score": ai_score},
        }
        return render(request, 'advisor/recommendations.html', context)

    return render(request, 'advisor/recommendations.html')
