# Refactorización con Design Patterns

Para la elaboración de este proyecto se utilizan los siguientes principios SOLID:

- Single Responsability Principle: cada clase creada en nuestro programa tiene una responsabilidad en específico de acuerdo a la tarea que se le fue asignada. Por ej: en WebReport y PrintReport tienen métodos que se utilizan para generar un formato distinto para web y en archivo de texto, y del cual no dependen el uno del otro.
- Open/Closed Principle: Las clases PrintReport y WebReport pueden extenderse sin necesidad de modificar previamente su contenido o tener alguna dependencia. Ej: puedo agregar un método en WebReport el cual genere estilos con css tags en el html, y esto no afectaria en PrintReport.
- Interface Segregation Principle: Aquí PrintReport y WebReport tienen las propiedades de la clase Report y si tuviera métodos también sería así. Si queremos generar una clase Report con o sin algún tipo de formato (WebReport o PrintReport) se puede hacer, así no tiene algún tipo de dependencia. De igual manera si generó un WebReport no necesito de los métodos de PrintReport.

# Patrones de diseño utilizados:

- Factory: Se utiliza para generar un tipo de objeto de acuerdo al reporte que se quiere generar. Como se puede ver en report_facade.py
- Facade: Se utiliza para manejar la lógica de generación de reportes de dos clases separadas en report_facade.py

# Building project locally

Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment. Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements

    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src

# Building Docker image

At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME
