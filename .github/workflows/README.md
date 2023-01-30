## Dossier workflows

**Contenu :**

Dans ce dossier, vous retrouverez les différents workflows utilisés, nous avons plusieurs GitHub Actions: 

* Une déclenchée à chaque changement pour builder l’application  ([flask_app_build.yaml](https://github.com/Naofel-eal/4A_SQR_CI-CD/blob/main/.github/workflows/flask_app_build.yaml))

[![Flask app build](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/flask_app_build.yaml/badge.svg)](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/flask_app_build.yaml)

* Une déclenchée manuellement pour builder et dockeriser et pousser l’image de l’API ([build_dockerfile.yml](https://github.com/Naofel-eal/4A_SQR_CI-CD/blob/main/.github/workflows/build_dockerfile.yml))

[![Docker Image Build](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/build_dockerfile.yaml/badge.svg)](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/build_dockerfile.yaml)

* Une déclenchée pour chaque tag semver pour builder et dockeriser et pousser l’image de l’API avec en tag la version semver spécifiée ([Build_and_Push_to_GCR.yaml](https://github.com/Naofel-eal/4A_SQR_CI-CD/blob/main/.github/workflows/Build_and_Push_to_GCR.yaml))

[![Docker push GCR](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/Build_and_Push_to_GCR.yaml/badge.svg)](https://github.com/Naofel-eal/4A_SQR_CI-CD/actions/workflows/Build_and_Push_to_GCR.yaml)

