from pathlib import Path
import sys
ROOT_DIR = Path(__file__).parent.parent.resolve() / 'src'
sys.path.append(ROOT_DIR.__str__())
