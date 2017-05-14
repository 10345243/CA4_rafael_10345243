
import unittest


from process_changes import Commit

class TestCommits(unittest.TestCase):

    changes_file = 'ca.txt'
    data = [line.strip() for line in open(changes_file, 'r')]
    sep = 72*'-'


    
    def test_number_of_lines(self):
        self.commit = Commit
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        self.commit = Commit
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        self.commit = Commit
        commits = get_commit_comment(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])

if __name__ == '__main__':
    unittest.main()
