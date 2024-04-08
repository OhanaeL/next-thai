# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    # Interactive Streamlit elements, like these sliders, return their value.
    # This gives you an extremely simple interaction model.
    start = st.sidebar.selectbox(
    'Starting Point',
    ('Email', 'Home phone', 'Mobile phone'))
    destinations = st.sidebar.multiselect(
    'Destination',
    ['Green', 'Yellow', 'Red', 'Blue'])
    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    duration = st.sidebar.date_input(
        "Duration Date",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
    cost = st.sidebar.slider('Managing Your Trip Costs', 3000, 20000, 10000, 1000)
    number = st.sidebar.number_input('Insert a number')
    destinations = st.sidebar.multiselect(
    'Trip Type',
    ['Green', 'Yellow', 'Red', 'Blue'])

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")
    )


if __name__ == "__main__":
    run()
