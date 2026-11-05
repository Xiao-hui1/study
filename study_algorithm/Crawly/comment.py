import csv
import re
from typing import NamedTuple


class Comment(NamedTuple):
    aid: list[str]
    bvid: list[str]
    cid: list[str]
    title: list[str]


class GetComment:
    """
    获取评论的类
    :param filename: 评论文件的路径
    """

    def __init__(self, filename: str):
        self.filename = filename

    def read_content(self) -> str:
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()

    def get_comments(self) -> Comment:
        content = self.read_content()
        aid = re.findall('"aid":(.*?),', content, re.S)
        bvid = re.findall('"bvid":"(.*?)",', content, re.S)
        cid = re.findall('"cid":(.*?),', content, re.S)
        title = re.findall('"title":"(.*?)"', content, re.S)

        return Comment(aid=aid, bvid=bvid, cid=cid, title=title)


class CommentWriter:
    def __init__(self, comments: Comment, filename: str):
        self.comments = comments
        self.filename = filename

    def write_to_csv(self):
        res = []
        for a in range(len(self.comments.title)):
            t = {
                "aid": self.comments.aid[a],
                "bvid": self.comments.bvid[a],
                "cid": self.comments.cid[a],
                "title": self.comments.title[a],
            }
            res.append(t)

        with open(self.filename, "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["aid", "bvid", "cid", "title"])
            writer.writeheader()
            writer.writerows(res)


if __name__ == "__main__":
    # 获取评论并写入 CSV 文件
    gc = GetComment("bilibili_comment.txt")
    comments = gc.get_comments()

    cw = CommentWriter(comments, "res_comment.csv")
    cw.write_to_csv()
