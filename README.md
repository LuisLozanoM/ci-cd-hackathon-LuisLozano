🚀 CI/CD Hackathon! 🛠️
🎯 Objetivo del Hackathon
Automatizar el ciclo de vida de una aplicación usando GitHub Actions y desplegarla en AWS (S3 o EC2), aplicando buenas prácticas de seguridad.
Cada participante podrá elegir entre:
Tecnología en la que estás especializado (Rol de LN)
Tecnología que no dominas
🏆 Se seleccionarán 2 ganadores:
Uno de la categoría de tecnología especializada
Uno de la categoría de tecnología no dominada
Debes de elegir una categoría solamente, si tomas el riesgo de la segunda categoría puedes competir contra menos concursantes, ¡tú decides!
 
Paso 1: Crear un Repositorio en GitHub
Repository name: ci-cd-hackaton-tunombre
Incluye un README.md con instrucciones claras del proyecto y pipeline.
Incluye en cuál categoría quieres concursar (Básico, Avanzado)
 
Paso 2: ⚙️Usar GitHub Actions para la configuración del CI Pipeline
 
Paso 3. ☁️ Despliegue en AWS
Opciones: Subida a S3, despliegue a EC2
 
Paso 4. 🔐 Buenas prácticas de seguridad
Debes implementar al menos 2 de las siguientes:
Usar GitHub Secrets para credenciales.
Limitar permisos del GITHUB_TOKEN a solo lectura si no se necesita más.
Evitar imprimir secretos en logs.
Usar OpenID Connect (OIDC) para autenticación sin claves largas.
 
Bonus: 🧪 Validación de calidad
Linting. Ej. ESLint, dotnet format
Pruebas unitarias. Ej. Jest, Mocha, xUnit, NUnit
Escaneo de seguridad. Ej npm audit, trivy, dotnet security Audit, Snyk              
Otro. Ej. Coverage reports, code complexity analysis, container security, etc.
 
📸 Evidencias Requeridas
Por favor incluye en tu repositorio o en un documento compartido:
Captura de pantalla del pipeline ejecutándose en GitHub Actions
Captura del despliegue exitoso en S3 o EC2
Captura del uso de GitHub Secrets u otra práctica de seguridad
Captura de resultados de linting, pruebas unitarias y escaneo de seguridad
Enlace al repositorio público
Veremos la última hora de modificación, si está editado a destiempo, descalificaaaaaaaaaaaaaaaad@.
 
📊 Rúbrica de Evaluación (100 puntos + 20 Bonus)

| Criterio | Puntos |
|----------|--------|
| CI/CD Pipeline funcional con GitHub Actions | 30 |
| Despliegue exitoso en AWS (S3 o EC2) | 30 |
| Implementación de buenas prácticas de seguridad | 25 |
| Claridad del README.md y evidencias | 15 |
| **Bonus:** Calidad del código (linting, pruebas, escaneo, OTRO) | 20 |
