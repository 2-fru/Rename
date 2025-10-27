
from pathlib import Path
import shutil


def get_file_path(input_dir: Path) -> list:
    """
    특정 폴더 내 파일들을 리스트에 저장한다.

    Params:
        - input_dir: 입력 폴더 경로

    Returns:
        - 파일 경로들
    """
    file_path_list = []

    for file_path in input_dir.iterdir():
        file_path_list.append(file_path)

    return file_path_list


def copy_and_rename_file(file_path_list: list, output_dir: Path, file_prefix: str):
    """
    파일명에서 특정 접두사를 제거하여 이름을 변경한다.

    Params:
        - file_path_list: 이름 수정할 파일들을 저장한 리스트
        - output_dir: 결과 저장 폴더 경로
        - file_prefix: 제거할 접두사
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in file_path_list:
        old_file_name = file_path.name
        new_file_name = old_file_name[len(file_prefix):]
        new_file_path = output_dir / new_file_name
        print(new_file_path)
        shutil.copy2(file_path, new_file_path)

    return


if __name__ == "__main__":
    input_dir = Path(r"Input")
    output_dir = Path("Output")

    file_prefix = "KakaoTalk_"

    file_path_list = get_file_path(input_dir)
    copy_and_rename_file(file_path_list, output_dir, file_prefix)
