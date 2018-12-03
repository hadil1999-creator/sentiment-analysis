# Sentiment Analysis

> A wrapper around Google Cloud AutoML & Google Cloud Natural Language for sentiment analysis

## Setup & Running

Please make sure to create the `GOOGLE_APPLICATION_CREDENTIALS` entry following the
instructions below:

1. In the GCP Console, go to the **Create service account key** page.
  > [Go to the Create Service Account Key page](https://console.cloud.google.com/apis/credentials/serviceaccountkey)
2. From the **Service account** drop-down list, select **New service account**.
3. In the **Service account name** field, enter a name .
4. From the **Role** drop-down list, select **Project > Owner**.
  > Note: The Role field authorizes your service account to access resources. You can view and
  > change this field later by using GCP Console. If you are developing a production app, specify
  > more granular permissions than Project > Owner. For more information, see granting roles to
  > service accounts.
4. Click Create. A JSON file that contains your key downloads to your computer. Please make sure to
provide it in the project root folder and rename it to `credentials.json`.

Then, you need to create and to activate the `venv` and install the requirements. Please make sure
to use Python 3. You may use [`asdf`](https://github.com/asdf-vm/asdf) to manage Python versions; a
`.tool-versions` file is already available.

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Once the setup is complete, you may run `python index.py`. The web server will be available at
port `3000` by default.

## Deployment

In order to deploy it, you may create a Docker image and then setup a Docker container. The following
commands may help on that:

```sh
$ docker build -t fiap/sentiment-analysis .
$ docker run -d -p 8080:80 fiap/sentiment-analysis:latest
```

The web server will be available at port `8080`.

## License

[MIT License](LICENSE) &copy; 2018-present Ewerton Carlos Assis, Felipe Ribeiro da Silva,
Alexandre Lima de Freitas
