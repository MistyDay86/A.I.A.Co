import shap
import lime
import lime.lime_tabular

# import a trained model from train_model.py

explainer = shap.Explainer(model)
shap_values = explainer.shap_values(X_train)

explainer.expected_value

def explain_1():
    shap.initjs()
    shap.force_plot(explainer.expected_value, shap_values[0, :], X.iloc[0, :])

def explain_2():
    shap.initjs()
    shap.decision_plot(explainer.expected_value, shap_values, feature_names=list(X.columns))

def explain_3():
    shap.initjs()
    shap.force_plot(explainer.expected_value, shap_values, X)

def explain_4():
    explainer_ebm = shap.Explainer(model.predict, X)
    shap_values_ebm = explainer_ebm(X_train)
    shap.initjs()
    shap.plots.beeswarm(shap_values_ebm)

def explain_5():
    shap_array = [0] * 21

    for j in range(21):
        cont = 0
        for i in range(478):
            cont += np.abs(shap_values_ebm.values[i][j])
        shap_array[j] = cont / 478
    return shap_array

def explain_6():
    shap.initjs()
    shap.dependence_plot('Percentage of loss in relation to the tenant total income', shap_values, X)

def explain_7():
    shap.initjs()
    shap.dependence_plot('Frequency of the rental fee', shap_values, X)

def explain_8():
    shap.initjs()
    shap.dependence_plot('Percentage of requested reduction compared to rental fee', shap_values, X)

def explain_9():
    shap.initjs()
    shap.plots._waterfall.waterfall_legacy(explainer.expected_value[0], shap_values[1], max_display=10, show=True)

def explain_10():
    shap.initjs()
    shap.summary_plot(shap_values, X_test.iloc[i], max_display=174, plot_type="bar")

def explain_11():
    shap.initjs()

    class ShapObject:

        def __init__(self, base_values, data, values, feature_names):
            self.base_values = base_values  # Single value
            self.data = data  # Raw feature values for 1 row of data
            self.values = values  # SHAP values for the same row of data
            self.feature_names = feature_names  # Column names

    shap_object = ShapObject(base_values=explainer.expected_value[0],
                             values=explainer.shap_values(X)[0, :],
                             feature_names=X.columns,
                             data=X.iloc[0, :])

    shap.plots._waterfall.waterfall_legacy(explainer.expected_value[0], shap_values[11], feature_names=df.columns,
                                           max_display=20, show=True)

explainer = lime.lime_tabular.LimeTabularExplainer(X.loc[:, :].values, feature_names=X_train.columns, verbose=True, mode='regression')
i = 10
explain_data_point = explainer.explain_instance(X_test.iloc[i], model.predict, num_features=21)

def explain_12():
    explain_data_point.as_pyplot_figure()

def explain_13():
    explain_data_point.as_list()

