import pytest
from FindTop.find_candidates import find_top_20


class Test_find_top_20():

    def test_find_top_20(self, load_data):
        candidates = load_data
        final_candidates = find_top_20(candidates)
        assert len(final_candidates) == 20

    @pytest.mark.parametrize('len_data', [30, 20])
    def test_2_find_top_20(self, identical_data, len_data):
        candidates = identical_data
        final_candidates = find_top_20(candidates)
        assert len(final_candidates) == len_data

    @pytest.mark.parametrize('len_data', [15])
    def test_3_find_top_20(self, identical_data_step, len_data):
        candidates = identical_data_step
        final_candidates = find_top_20(candidates, len_candidates=3)
        assert len(final_candidates) == 3
