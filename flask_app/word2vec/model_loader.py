from gensim.models import KeyedVectors
import pickle

# グローバル変数としてモデルを定義
ja_model = None

#モデルをロード
def load_model(model_path, pickle_path, model_name):
    global ja_model
    if model_name == 'ja_model' and ja_model is None:
        print(f"Loading {model_name} from file...")
        ja_model = KeyedVectors.load_word2vec_format(model_path, binary=False)
        print(f"{model_name} loaded.")
        with open(pickle_path, 'wb') as f:
            pickle.dump(ja_model, f)
        print(f"{model_name} saved to pickle file.")
    else:
        print(f"{model_name} already loaded.")

#モデルをピクルからロード
def load_model_from_pickle(pickle_path, model_name):
    global ja_model, en_model
    if model_name == 'ja_model' and ja_model is None:
        print(f"Loading {model_name} from pickle file...")
        with open(pickle_path, 'rb') as f:
            ja_model = pickle.load(f)
        print(f"{model_name} loaded from pickle file.")
    else:
        print(f"{model_name} already loaded.")
#モデルを取得
def get_model(model_name):
    if model_name == 'ja_model' and ja_model is None:
        raise ValueError("ja_model has not been loaded yet.")
    return ja_model if model_name == 'ja_model' else en_model

if __name__ == "__main__":
    load_model('models/ja_model.vec', 'models/ja_model.pickle', 'ja_model')
    try:
        ja_model = get_model('ja_model')
        print("Both models are available for use.")
    except ValueError as e:
        print(e)
