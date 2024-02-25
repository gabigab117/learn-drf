import requests


ECOSCORE_GRADE = "b"


def mock_openfoodfact_success(self, method, url):
    # Notre mock doit avoir la même signature que la méthode à mocker
    # À savoir les paramètres d'entrée et le type de sortie
    def monkey_json():
        return {"product": {'ecoscore_grade': ECOSCORE_GRADE}}

    response = requests.Response()
    response.status_code = 200
    response.json = monkey_json
    # Attention à ne pas mettre les (), nous n'appelons pas la méthode mais la remplaçons
    return response
