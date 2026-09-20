"""
🧭 This test file turns each JSON case into its own unittest so every
scenario gets clear pass/fail reporting, plus a small timeout guard.

Instead of putting all cases inside one big `test()` loop, we generate
one real test method per case. That way, `unittest` can show exactly
which scenario passed or failed in verbose mode. 
"""

import json
import os
import time
import unittest
from typing import Dict, List, Optional
from timeout_decorator import TimeoutError, timeout
from source.solution import Solution
from listnode import ListNode

def _to_test_name(title: str) -> str:
    # 🏷️ Convert each friendly title into a safe unittest method name.
    sanitized   = ''.join(char.lower() if char.isalnum() else '_' for char in title)
    compact     = '_'.join(part for part in sanitized.split('_') if part)
    return f'test_{compact}'

def _create_linked_list(values: List[int]) -> Optional[ListNode]:
    # 🔗 Build a linked list from the given values.
    if not values: return None

    head    = ListNode(values[0])
    current = head

    for index in range(1, len(values)):
        new_node        = ListNode(values[index])
        current.next    = new_node
        current         = new_node

    return head

def _make_testcase(testcase):
    # 🧱 Build one real unittest method per JSON case for better test output.
    def test_method(self):
        title           :   str         = testcase['title']
        list            :   List[int]   = testcase['input']['head']
        k               :   int         = testcase['input']['k']
        expected_output :   List[int]   = testcase['output']
        description     :   str         = testcase.get('description', 'No description provided.')
        
        self._case_title        = title
        self._case_description  = description

        print('\n' + '=' * 60)
        print(f'🧪 Test Case : {title}')
        print(f'🤔 Scenario  : {description}')
        print(f'📝 Input : List={list}')
        print(f'📝 Input : k={k}')
        print('⏳ Starting soon...')
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        try:
            list_head: Optional[ListNode] = _create_linked_list(values=list)
            actual_output: List[int] = self._run_case(list_head=list_head, k=k)
        except TimeoutError:
            print(f'⏱️ Result    : Time Limit Exceeded in {title}')
            print('=' * 60)
            self.fail(f'⏱️ Time Limit Exceeded: {title}')

        if actual_output == expected_output:
            print(f'✅ Result    : Passed with answer {actual_output}')
        else:
            print(f'❌ Result    : Expected {expected_output}, got {actual_output}')

        print('=' * 60)
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        self.assertEqual(
            actual_output,
            expected_output,
            f'❌ Value Mismatch in {title}\n'
            f'Expected = {expected_output}\n'
            f'Actual   = {actual_output}'
        )

    return test_method


class TestSolution(unittest.TestCase):
    # 🎛️ Tweak this to make the test run faster or more cinematic.
    DISPLAY_DELAY_SECONDS = 2
    CASE_RESULTS: List[Dict[str, str]] = []

    def setUp(self):
        # 🛠️ Each test gets a fresh solution instance to keep runs predictable.
        self.__solution = Solution()
        return super().setUp()

    @timeout(1)
    def _run_case(self, list_head: Optional[ListNode], k: int) -> List[int]:
        # ⚡ Give every testcase its own timeout instead of timing the whole file.
        head: Optional[ListNode] = self.__solution.rotateRight(list_head, k)
        result: List[int] = []

        while head:
            result.append(head.val)
            head = head.next

        return result

class RotateListTestResult(unittest.TextTestResult):
    # 🧾 Capture each testcase outcome so we can print one final summary.
    def addSuccess(self, test):
        super().addSuccess(test)
        TestSolution.CASE_RESULTS.append(
            {
                'title': getattr(test, '_case_title', test._testMethodName),
                'status': '✅ Passed',
            }
        )

    def addFailure(self, test, err):
        super().addFailure(test, err)
        TestSolution.CASE_RESULTS.append(
            {
                'title': getattr(test, '_case_title', test._testMethodName),
                'status': '❌ Failed',
            }
        )

    def addError(self, test, err):
        super().addError(test, err)
        TestSolution.CASE_RESULTS.append(
            {
                'title': getattr(test, '_case_title', test._testMethodName),
                'status': '💥 Error',
            }
        )

    def stopTestRun(self):
        super().stopTestRun()

        print('\n' + '🧾' + '=' * 58)
        print('📚 Rotate List Final Summary')

        if not TestSolution.CASE_RESULTS:
            print('No test cases were executed.')
            print('=' * 60)
            return

        passed_count    = sum(result['status'] == '✅ Passed' for result in TestSolution.CASE_RESULTS)
        failed_count    = sum(result['status'] == '❌ Failed' for result in TestSolution.CASE_RESULTS)
        error_count     = sum(result['status'] == '💥 Error' for result in TestSolution.CASE_RESULTS)
        success_rate    = (passed_count / len(TestSolution.CASE_RESULTS)) * 100
        title_width     = max(len('Test Case'), *(len(result['title']) for result in TestSolution.CASE_RESULTS))
        status_width    = max(len('Status'), *(len(result['status']) for result in TestSolution.CASE_RESULTS))

        divider = f"+-{'-' * title_width}-+-{'-' * status_width}-+"
        header  = f"| {'Test Case'.ljust(title_width)} | {'Status'.ljust(status_width)} |"

        print(divider)
        print(header)
        print(divider)
        for result in TestSolution.CASE_RESULTS:
            print(f"| {result['title'].ljust(title_width)} | {result['status'].ljust(status_width)} |")
        print(divider)

        print(
            f'🏁 Total: {len(TestSolution.CASE_RESULTS)} | '
            f'✅ Passed: {passed_count} | '
            f'❌ Failed: {failed_count} | '
            f'💥 Errors: {error_count}'
        )
        print(f'📈 Success Rate: {success_rate:.2f}%')
        print('=' * 60)


_CURRENT_DIRECTORY  = os.path.dirname(os.path.abspath(__file__))
_FILE_PATH          = os.path.join(_CURRENT_DIRECTORY, 'cases.json')


with open(_FILE_PATH, mode='r', encoding='utf-8') as read_file:
    all_testcases = json.load(read_file)

    # 🧪 Register every case as a standalone test so verbose mode is meaningful.
    for testcase in all_testcases:
        setattr(TestSolution, _to_test_name(testcase['title']), _make_testcase(testcase))


if __name__ == '__main__':
    unittest.main(
        verbosity=2,
        testRunner=unittest.TextTestRunner(resultclass=RotateListTestResult)
    )
