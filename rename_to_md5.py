
from pathlib import Path
import hashlib
import shutil


def get_file_path(input_dir) -> list:
    """
    특정 폴더 내 파일들을 리스트에 저장한다.

    Params:
        - input_dir: 입력 폴더 경로 (<class 'pathlib.WindowsPath'>)

    Returns:
        - 파일 경로들
    """
    file_path_list = []

    for file_path in input_dir.iterdir():
        file_path_list.append(file_path)

    return file_path_list


def copy_and_rename_file(file_path_list: list, output_dir):
    """
    해당 파일의 MD5 값으로 파일명을 변경한다.

    Params:
        - file_path_list: 입력 파일 경로들
        - output_dir: 결과 저장 폴더 경로
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in file_path_list:
        old_file = file_path
        old_file_bytes = open(old_file, "rb").read()
        old_file_md5 = hashlib.md5(old_file_bytes).hexdigest()

        new_file = old_file_md5 + old_file.suffix
        new_file = output_dir / new_file
        shutil.copy2(old_file, new_file)
    return


if __name__ == "__main__":
    input_dir = Path(r"Input")
    output_dir = Path(r"Output")

    file_path_list = get_file_path(input_dir)
    copy_and_rename_file(file_path_list, output_dir)
    print(f"\n{input_dir} -> {output_dir} 완료")
