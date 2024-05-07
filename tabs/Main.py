import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
points_scored = np.random.randint(0, 20, 100)  # Points scored per match
points_allowed = np.random.randint(0, 20, 100)  # Points allowed per match
takedowns = np.random.randint(0, 10, 100)


# Graph 2: Boxplot of Points Scored vs. Allowed
def points_scored_allowed():
    st.header("Graph 2: Boxplot Comparison of Points Scored vs. Allowed")
    fig2, ax2 = plt.subplots()
    ax2.boxplot([points_scored, points_allowed], labels=['Points Scored', 'Points Allowed'])
    ax2.set_title('Points Scored vs. Points Allowed per Match')
    ax2.set_ylabel('Points')
    st.pyplot(fig2)
    st.markdown("**Interpretation**: This boxplot compares the points scored by athletes versus the points they allowed in matches. Coaches can identify areas of strength and needed improvement.")



# Graph 3: Scatter plot of Points Scored vs. Takedowns
def scatter_points():
    st.header("Graph 3: Scatter Plot of Points Scored vs. Takedowns")
    fig3, ax3 = plt.subplots()
    ax3.scatter(takedowns, points_scored, color='blue', alpha=0.7)
    ax3.set_title('Relationship between Takedowns and Points Scored')
    ax3.set_xlabel('Takedowns per Match')
    ax3.set_ylabel('Points Scored per Match')
    st.pyplot(fig3)
    st.markdown("**Interpretation**: This scatter plot highlights the correlation between takedowns and points scored. A strong positive correlation would indicate that takedowns are an effective offensive strategy.")


# Data simulation
dates = np.arange(np.datetime64('2024-01-01'), np.datetime64('2024-12-31'))
recovery_days = np.random.poisson(1, len(dates))  # Randomly generate recovery days

# Create a line plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(dates, recovery_days, label='Recovery Days')
    ax.set_title('Recovery and Injury Tracking Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Recovery Days')
    ax.legend()
    st.pyplot(fig)
    st.markdown("**Interpretation**: This chart tracks the days spent in recovery from training sessions or injuries. Monitoring this can help ensure that you are getting enough rest and can adjust your training intensity or focus on specific recovery techniques as needed.")


def show():
    def page_stylable_container1():
        with stylable_container(
            key="Blue",
            css_styles="""
                {
                    height: "500"px;
                    background-color: #3F9EED80;
                    color: #e6e6e6;
                    border-radius: 5px;
                    padding: 15px;
                    margin: 10px;
                    border: 1px solid #ccc;
                    box-shadow: 0px 0px 8px #FFCB0B;
                    overflow-x: auto;
                }
            """,
        ):
            st.markdown("This is the Athelete's Personally tailored page")
    
    page_stylable_container1()


    #first box
    def container1():
        return st.container(border=True)
    def container1a():
        return st.container(border=True)
    def container1b():
        return st.container(border=True)
    def container1c():
        return st.container(border=True)
    def container1c1():
        return st.container(border=True)
    #second box
    def container2():
        return st.container(border=True)
    def container2a():
        return st.container(border=True)
    def container2b():
        return st.container(border=True)
    def container2c():
        return st.container(border=True)

    with container1():
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,10,1,5,1,7,1])
        with col2:
            with container1a():
                points_scored_allowed()
        with col4:
            with container1b():
                scatter_points()
        with col6:
            with container1c():
                st.write("containers can be extremely versatile and section off or bring attention to different parts of the UI")
            with container1c1():
                line_plot()
    with container2():
        col1_1, col2_1, col3_1, col4_1, col5_1, col6_1, col7_1 = st.columns([1,6,1,4,1,4,1])
        with col2_1:
            with container2a():
                scatter_points()
        with col4_1:
            with container2b():
                st.markdown("""
# Workout Plan for Optimal Performance

Based on your current goals, here are some workout routines I can recommend:

## Strength Training
- **Squats**: 3 sets of 8-10 reps
- **Deadlifts**: 3 sets of 8-10 reps
- **Bench Press**: 3 sets of 8-10 reps
- **Pull-ups**: 3 sets of as many reps as possible

## Cardiovascular Endurance
- **Interval Running**: 20 minutes of alternating between sprinting for 1 minute and jogging for 2 minutes.
- **Stair Climbing**: 15 minutes at a vigorous pace.
- **Rowing Machine**: 20 minutes with varying intensity.

## Agility Drills
- **Ladder Drills**: Various footwork patterns for 10 minutes.
- **Cone Drills**: Zigzag and shuttle runs for agility and speed enhancement.
- **Box Jumps**: 3 sets of 10 reps for explosive power.

## Flexibility and Recovery
- **Yoga**: 30-minute sessions focusing on flexibility and core strength.
- **Foam Rolling**: 15 minutes focusing on major muscle groups to aid recovery.
- **Dynamic Stretching**: 10 minutes before each workout session to reduce injury risk.

## Wrestling Specific Drills
- **Takedown Practice**: Drill various takedown techniques with a partner.
- **Mat Work**: Practice controlling an opponent on the mat using grips and body weight.
- **Defense Drills**: Work on blocking and escaping from holds and grips.

## Weekly Schedule
- **Monday**: Strength Training + Flexibility and Recovery
- **Tuesday**: Cardiovascular Endurance + Wrestling Specific Drills
- **Wednesday**: Agility Drills + Flexibility and Recovery
- **Thursday**: Strength Training + Wrestling Specific Drills
- **Friday**: Cardiovascular Endurance + Agility Drills
- **Saturday**: Active Recovery or Light Yoga
- **Sunday**: Rest

Remember, consistency is key in any training regimen. Adjust the intensity and volume based on your current fitness level and competition schedule.
""")

        with col6_1:
            with container2c():
                st.markdown("""
# Nutrition Plan for Optimal Performance

Based on your current goals, here are some foods and dishes I can recommend:

## Breakfast Options
- **Oatmeal** with banana slices and a spoon of peanut butter.
- **Greek yogurt** with mixed berries and granola.
- **Scrambled eggs** with spinach, mushrooms, and whole-grain toast.

## Lunch Options
- **Grilled chicken breast** with quinoa and steamed broccoli.
- **Turkey and avocado wrap** with a whole wheat tortilla and a side of cottage cheese.
- **Lentil soup** with a mixed green salad and vinaigrette dressing.

## Dinner Options
- **Baked salmon** with sweet potato and green beans.
- **Beef stir-fry** with bell peppers, broccoli, and brown rice.
- **Pasta** with lean ground turkey and marinara sauce, served with a side salad.

## Snack Options
- Almonds and a piece of fruit (apple or orange).
- Protein shake with whey protein, almond milk, and a handful of spinach.
- Hummus with carrot and celery sticks.

## Hydration
- Consistent water intake throughout the day.
- Electrolyte-infused water post-training.
- Green tea as a healthy, antioxidant-rich beverage option.
""")
